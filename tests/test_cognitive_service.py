from smos.core.database import SessionLocal
from smos.models.models import User, Timeline, TimelineType
from smos.services.cognitive_service import CognitiveService

def test_cognitive_service():
    db = SessionLocal()
    user = db.query(User).first()
    timeline = db.query(Timeline).first()

    svc = CognitiveService(db)

    # Session
    session = svc.create_session(workspace_id=None, topic="AI Architecture", timeline_id=timeline.id, participants=[user.id])
    assert session.topic == "AI Architecture"

    # Thought
    thought = svc.add_thought(user.id, timeline.id, "We should use a graph database.")
    assert thought.author_id == user.id
    assert "graph" in thought.content

    db.close()

if __name__ == "__main__":
    test_cognitive_service()
