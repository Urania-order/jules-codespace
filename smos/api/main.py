from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from smos.core.database import get_db
from smos.models.models import Event as DBEvent, User, Workspace, MemoryNode
from smos.services.embedding_service import embedding_service
from smos.services.orchestrator import AgentOrchestrator
from smos.services.permissions import PermissionService
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime
from pgvector.sqlalchemy import Vector

app = FastAPI(title="Co-SMOS API", version="0.1")

class EventCreate(BaseModel):
    user_id: int
    workspace_id: Optional[int] = None
    type: str
    content: Dict[str, Any]

@app.get("/")
def read_root():
    return {"message": "Welcome to Co-SMOS API"}

@app.post("/event")
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    if event.workspace_id:
        PermissionService.verify_workspace_access(db, event.user_id, event.workspace_id)

    db_event = DBEvent(
        user_id=event.user_id,
        workspace_id=event.workspace_id,
        type=event.type,
        content=event.content
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)

    # Trigger Orchestrator
    orchestrator = AgentOrchestrator(db)
    orchestrator.on_event(db_event)

    return db_event

@app.get("/events")
def get_events(db: Session = Depends(get_db)):
    return db.query(DBEvent).all()

@app.get("/memory/search")
def search_memory(q: str, user_id: int, limit: int = 20, db: Session = Depends(get_db)):
    # Basic permission check: only return public or owned nodes
    # (In a real system, we'd also check workspace memberships)
    embedding = embedding_service.get_embedding(q)
    results = db.query(MemoryNode).filter(
        (MemoryNode.owner_id == user_id) | (MemoryNode.workspace_id.isnot(None))
    ).order_by(
        MemoryNode.embeddings.l2_distance(embedding)
    ).limit(limit).all()

    return [
        {
            "id": r.id,
            "content": r.content,
            "type": r.type,
            "reality_level": r.reality_level
        }
        for r in results
    ]
