import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from smos.core.database import Base
from smos.models.models import MemoryNode, KnowledgeLifecycleState, EpistemicStatus
from smos.services.value_physics_engine import ValuePhysicsEngine
from smos.services.evolution_service import EvolutionService
from smos.services.attention_ecology_service import AttentionEcologyService
from smos.models.discovery import Hypothesis

@pytest.fixture
def db():
    engine = create_engine("sqlite:///:memory:")
    # Ensure all models are loaded so create_all works with FKs
    from smos.models import models, goals, consensus, discussion, cognitive, entities, experience, epistemic, discovery, coevolution, ecology
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    yield db
    db.close()

def test_value_physics_engine(db):
    node = MemoryNode(content="Test Knowledge", importance=0.8)
    db.add(node)
    db.commit()

    engine = ValuePhysicsEngine(db)
    metrics = engine.update_node_physics(node.id)
    assert metrics["energy"] >= 0.0
    assert metrics["potential"] == 0.8

def test_knowledge_lifecycle(db):
    node = MemoryNode(content="Seed Idea", lifecycle_state=KnowledgeLifecycleState.IDEA)
    db.add(node)
    db.commit()

    svc = EvolutionService(db)
    # Idea -> Discussion
    updated_node = svc.advance_lifecycle(node.id)
    assert updated_node.lifecycle_state == KnowledgeLifecycleState.DISCUSSION

    # Discussion -> Recipe
    updated_node = svc.advance_lifecycle(node.id)
    assert updated_node.lifecycle_state == KnowledgeLifecycleState.RECIPE

def test_attention_ecology(db):
    node1 = MemoryNode(content="Hidden Gem")
    db.add(node1)
    db.commit()

    # Manually add a value assessment with low knowledge value but high social impact
    from smos.models.ecology import ValueAssessment
    va = ValueAssessment(node_id=node1.id, knowledge_value=0.1, social_impact=0.9)
    db.add(va)
    db.commit()

    svc = AttentionEcologyService(db)
    recommendations = svc.recommend_under_discovered()
    assert len(recommendations) > 0
    assert recommendations[0].content == "Hidden Gem"
