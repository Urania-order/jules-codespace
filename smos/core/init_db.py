from smos.core.database import engine, Base
from smos.models.models import User, Workspace, Timeline, MemoryNode, Relation, Event, Stream
from smos.models.goals import Goal, Task
from smos.models.consensus import Proposal, Vote
from smos.models.discussion import Comment, Reaction

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database tables created.")

if __name__ == "__main__":
    init_db()
