from sqlalchemy.orm import Session
from smos.models.ecology import ValueAssessment, KnowledgeActivation, KnowledgeImpact
from smos.models.models import MemoryNode
from typing import Dict, Any
from datetime import datetime, timezone

class ValuePhysicsEngine:
    def __init__(self, db: Session):
        self.db = db

    def calculate_metrics(self, node_id: int) -> Dict[str, float]:
        """
        Calculate dynamic metrics based on node activity and history.
        """
        activations = self.db.query(KnowledgeActivation).filter(KnowledgeActivation.node_id == node_id).first()
        impacts = self.db.query(KnowledgeImpact).filter(KnowledgeImpact.source_node_id == node_id).all()

        usage_count = activations.usage_count if activations else 0
        impact_count = len(impacts)

        # Knowledge Energy: Base activity + impacts
        energy = min(1.0, (usage_count * 0.1) + (impact_count * 0.2))

        # Knowledge Momentum: Rate of change (mocked as usage relative to time)
        momentum = 0.5 if usage_count > 0 else 0.0

        # Knowledge Resonance: Impact confidence
        resonance = sum(i.confidence for i in impacts) / impact_count if impact_count > 0 else 0.1

        # Knowledge Potential: Estimated based on type and importance
        node = self.db.query(MemoryNode).get(node_id)
        potential = node.importance if node else 0.5

        return {
            "energy": energy,
            "momentum": momentum,
            "potential": potential,
            "resonance": resonance,
            "entropy": 0.1, # Measure of fragmentation
            "diffusion": min(1.0, impact_count * 0.25)
        }

    def update_node_physics(self, node_id: int):
        metrics = self.calculate_metrics(node_id)
        assessment = self.db.query(ValueAssessment).filter(ValueAssessment.node_id == node_id).first()
        if not assessment:
            assessment = ValueAssessment(node_id=node_id)
            self.db.add(assessment)

        assessment.knowledge_value = metrics["energy"] * metrics["resonance"]
        assessment.social_impact = metrics["diffusion"]

        self.db.commit()
        return metrics
