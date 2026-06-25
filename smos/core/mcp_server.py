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
