from smos.core.database import engine, Base
from smos.models.models import User, Workspace, Timeline, MemoryNode, Relation, Event
from smos.models.goals import Goal, Task

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database tables created.")

if __name__ == "__main__":
    init_db()
