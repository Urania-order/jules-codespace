from mcp.server.fastmcp import FastMCP
from smos.core.database import SessionLocal
from smos.services.integrations import JulesService
from typing import List

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

@mcp.tool()
def compare_timelines(id_a: int, id_b: int) -> str:
    """Compare two timelines and find differences"""
    db = SessionLocal()
    from smos.services.timeline_service import TimelineService
    svc = TimelineService(db)
    result = svc.compare_timelines(id_a, id_b)
    db.close()
    return f"Timeline Comparison: {result}"

@mcp.tool()
def create_recipe(title: str, author_id: int, steps: List[str], problem_type: str) -> str:
    """Create a new successful recipe for solving a problem"""
    db = SessionLocal()
    from smos.services.recipe_service import RecipeService
    svc = RecipeService(db)
    recipe = svc.create_recipe(title, author_id, steps, problem_type)
    recipe_id = recipe.id
    db.close()
    return f"Recipe created with ID: {recipe_id}"

@mcp.tool()
def start_cognitive_session(topic: str, timeline_id: int, participants: List[int]) -> str:
    """Start a collective thinking session on a specific topic"""
    db = SessionLocal()
    from smos.services.cognitive_service import CognitiveService
    svc = CognitiveService(db)
    session = svc.create_session(None, topic, timeline_id, participants)
    session_id = session.id
    db.close()
    return f"Cognitive Session started with ID: {session_id}"
