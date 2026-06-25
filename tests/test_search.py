import httpx
import time
import subprocess
import os
from smos.core.database import SessionLocal
from smos.models.models import User, Event, Timeline, TimelineType
from smos.services.memory_service import MemoryService

def test_search():
    # Setup data
    db = SessionLocal()
    user = db.query(User).first()
    if not user:
        user = User(display_name="Search Test User")
        db.add(user)
        db.commit()
        db.refresh(user)

    service = MemoryService(db)

    # Add some memories
    m1 = service.process_event(Event(user_id=user.id, content={"text": "The capital of France is Paris"}))
    m2 = service.process_event(Event(user_id=user.id, content={"text": "Apple makes iPhones"}))
    m3 = service.process_event(Event(user_id=user.id, content={"text": "FastAPI is a modern web framework"}))

    user_id = user.id
    db.close()

    # Start server
    proc = subprocess.Popen(
        ["uvicorn", "smos.api.main:app", "--host", "127.0.0.1", "--port", "8001"],
        env=dict(os.environ, PYTHONPATH=".")
    )
    time.sleep(3)

    try:
        # Search for something related to FastAPI
        response = httpx.get(f"http://127.0.0.1:8001/memory/search?q=FastAPI framework&user_id={user_id}")
        print(f"Search Results: {response.json()}")
        assert response.status_code == 200
        assert len(response.json()) > 0

        # Check if FastAPI is in any of the results since we use dummy embeddings
        contents = [r["content"] for r in response.json()]
        assert any("FastAPI" in c for c in contents)

    finally:
        proc.terminate()

if __name__ == "__main__":
    test_search()
