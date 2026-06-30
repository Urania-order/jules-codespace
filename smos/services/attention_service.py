from sqlalchemy.orm import Session
from smos.models.models import MemoryNode
from smos.models.ecology import ValueAssessment
from sqlalchemy import desc

class AttentionService:
    def __init__(self, db: Session):
        self.db = db

    def recommend_valuable_knowledge(self, limit: int = 5):
        """Recommend knowledge based on long-term value and low current activation (under-discovered)"""
        # Focus on high potential but low activation
        results = self.db.query(ValueAssessment).filter(
            ValueAssessment.potential > 0.7,
            ValueAssessment.activation < 0.3
        ).order_by(desc(ValueAssessment.potential)).limit(limit).all()

        recommendations = []
        for assessment in results:
            node = self.db.query(MemoryNode).get(assessment.node_id)
            if node:
                recommendations.append({
                    "node_id": node.id,
                    "content": node.content[:100],
                    "potential": assessment.potential,
                    "reason": "High potential impact, but under-utilized in the current ecology."
                })

        return recommendations

    def allocate_attention(self, node_id: int):
        """Increase activation for a piece of knowledge"""
        assessment = self.db.query(ValueAssessment).filter(ValueAssessment.node_id == node_id).first()
        if assessment:
            assessment.activation += 0.1
            assessment.momentum += 0.05
            self.db.commit()
            return True
        return False
