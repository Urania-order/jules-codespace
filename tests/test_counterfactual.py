from smos.core.database import SessionLocal
from smos.models.models import User, Timeline, TimelineType
from smos.services.counterfactual_engine import CounterfactualEngine

def test_counterfactual():
    db = SessionLocal()
    user = db.query(User).first()

    # Get main timeline
    main_timeline = db.query(Timeline).filter(Timeline.type == TimelineType.REAL).first()

    engine = CounterfactualEngine(db)

    # Branch
    alt_timeline = engine.branch_timeline(
        parent_id=main_timeline.id,
        description="What if we used Neo4j?"
    )
    print(f"Created Timeline: {alt_timeline.id}, description: {alt_timeline.description}")
    assert alt_timeline.parent_timeline_id == main_timeline.id

    # Create counterfactual memory
    cf_memory = engine.create_counterfactual_memory(
        timeline_id=alt_timeline.id,
        content="Neo4j provides better graph traversal for semantic memory.",
        owner_id=user.id
    )
    print(f"Created CF Memory: {cf_memory.id}, level: {cf_memory.reality_level}")
    assert cf_memory.timeline_id == alt_timeline.id
    assert cf_memory.reality_level == "COUNTERFACTUAL"

    db.close()

if __name__ == "__main__":
    test_counterfactual()
