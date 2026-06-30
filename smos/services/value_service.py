from sqlalchemy.orm import Session
from smos.models.ecology import ValueAssessment
from typing import Dict, Any

class ValueService:
    def __init__(self, db: Session):
        self.db = db

    def assess_knowledge_value(self, node_id: int, human_benefit: float, environmental_impact: float, social_impact: float = 0.0):
        """Principle: Value requires human benefit"""
        knowledge_value = (human_benefit + (1.0 - environmental_impact) + social_impact) / 3.0

        # Calculate dynamic physics metrics (Mock logic for v0.8 transition)
        energy = human_benefit * 0.8 + social_impact * 0.2
        momentum = 0.1 # Initial momentum
        potential = 1.0 - environmental_impact
        entropy = 0.05
        resonance = (human_benefit + social_impact) / 2.0

        assessment = ValueAssessment(
            node_id=node_id,
            knowledge_value=knowledge_value,
            human_benefit=human_benefit,
            environmental_impact=environmental_impact,
            social_impact=social_impact,
            energy=energy,
            momentum=momentum,
            potential=potential,
            entropy=entropy,
            activation=0.0,
            dormancy=0.0,
            regeneration=0.0,
            decay=0.0,
            resonance=resonance,
            diffusion=0.0,
            uncertainty=0.1
        )
        self.db.add(assessment)
        self.db.commit()
        self.db.refresh(assessment)
        return assessment

    def recalculate_physics(self, assessment_id: int):
        assessment = self.db.query(ValueAssessment).get(assessment_id)
        if not assessment:
            return None

        # In a real system, these would be influenced by usage, time, and resonance
        assessment.momentum *= 1.1 # Mock increase
        assessment.entropy += 0.01 # Mock increase over time
        assessment.decay = assessment.entropy * 0.5

        self.db.commit()
        self.db.refresh(assessment)
        return assessment

    def verify_human_meaning_principle(self, assessment_id: int):
        assessment = self.db.query(ValueAssessment).get(assessment_id)
        if assessment and assessment.human_benefit > 0.5:
            return True
        return False
