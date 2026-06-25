from mcp.server.fastmcp import FastMCP
from smos.core.database import SessionLocal
from smos.services.integrations import JulesService

mcp = FastMCP("smos")

@mcp.tool()
def search_memory(query: str) -> str:
    """Search semantic memory"""
    db = SessionLocal()
    from smos.models.models import MemoryNode
    from smos.services.embedding_service import embedding_service
    embedding = embedding_service.get_embedding(query)
    results = db.query(MemoryNode).order_by(
        MemoryNode.embeddings.l2_distance(embedding)
    ).limit(3).all()
    db.close()
    return f"Found: {[r.content for r in results]}"

@mcp.tool()
def create_jules_session(task: str, repo: str = None) -> str:
    """Create a new Jules session"""
    jules = JulesService()
    result = jules.create_session(task, repo)
    return f"Jules session created: {result}"

@mcp.tool()
def get_clipboard() -> str:
    """Get current clipboard content (Mock)"""
    return "Clipboard content: 'Sample text from clipboard'"

@mcp.tool()
def set_clipboard(text: str) -> str:
    """Set clipboard content (Mock)"""
    return f"Clipboard set to: {text}"

@mcp.tool()
def create_task(title: str, goal_id: int = None) -> str:
    """Create a new task"""
    db = SessionLocal()
    from smos.models.goals import Task
    task = Task(title=title, goal_id=goal_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    task_id = task.id
    db.close()
    return f"Task created with ID: {task_id}"

@mcp.tool()
def get_active_goals(user_id: int) -> str:
    """Get active goals for a user"""
    db = SessionLocal()
    from smos.services.goal_engine import GoalEngine
    engine = GoalEngine(db)
    goals = engine.identify_active_projects(user_id)
    db.close()
    return f"Active goals: {[g.title for g in goals]}"
