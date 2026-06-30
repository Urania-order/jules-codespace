from sqlalchemy.orm import Session
from smos.models.models import MemoryNode
from smos.models.ecology import ValueAssessment
from typing import List

class AttentionEcologyService:
    def __init__(self, db: Session):
        self.db = db

    def recommend_under_discovered(self, limit: int = 5) -> List[MemoryNode]:
        """
        Recommend knowledge that has high Potential but low current Energy/Popularity.
        """
        # Join MemoryNode with ValueAssessment to find high potential nodes with low energy
        # In a real system, this would be a single optimized query
        assessments = self.db.query(ValueAssessment).filter(
            ValueAssessment.knowledge_value < 0.3 # Low energy/value current
        ).order_by(ValueAssessment.social_impact.desc()).limit(limit).all()

        node_ids = [a.node_id for a in assessments]
        return self.db.query(MemoryNode).filter(MemoryNode.id.in_(node_ids)).all()

    def highlight_successful_recipes(self) -> List[MemoryNode]:
        """Identify recipes that have led to verified collective outcomes"""
        from smos.models.models import KnowledgeLifecycleState
        return self.db.query(MemoryNode).filter(
            MemoryNode.lifecycle_state == KnowledgeLifecycleState.COLLECTIVE_EXPERIENCE
        ).all()
