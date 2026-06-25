from smos.core.database import SessionLocal
from smos.models.models import MemoryNode, User, Timeline, TimelineType
from smos.services.epistemic_service import EpistemicService

def test_epistemic_service():
    db = SessionLocal()

    user = User(display_name="Epistemic User")
    db.add(user)
    db.commit()

    tl = Timeline(type=TimelineType.REAL)
    db.add(tl)
    db.commit()

    node = MemoryNode(content="Ancient aliens built the pyramids", owner_id=user.id, timeline_id=tl.id)
    db.add(node)
    db.commit()

    svc = EpistemicService(db)
    layer = svc.create_layer("MYTHOLOGY", 0.1, "TRADITIONAL")

    updated_node = svc.assign_to_layer(node.id, layer.id, "BEYOND_CONSENSUS")
    assert layer.id in updated_node.layer_ids
    assert updated_node.epistemic_status == "BEYOND_CONSENSUS"

    bc_nodes = svc.get_beyond_consensus_nodes()
    assert len(bc_nodes) > 0

    db.close()

if __name__ == "__main__":
    test_epistemic_service()
