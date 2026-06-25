from smos.core.database import SessionLocal
from smos.services.reconstruction_service import ReconstructionService
from smos.models.models import Event

def test_reconstruction_service():
    db = SessionLocal()
    svc = ReconstructionService(db)

    # Ensure all tables are recognized by SQLA in this session
    # This sometimes helps with circular dependency issues in tests
    from smos.models.models import Event
    from smos.models.experience import Reconstruction

    rec = svc.reconstruct_event([{"type": "log", "content": "Server error at 10:00"}], 0.8)
    assert rec.confidence == 0.8
    assert "reconstructed" in rec.inferred_facts["status"]

    db.close()

if __name__ == "__main__":
    test_reconstruction_service()
