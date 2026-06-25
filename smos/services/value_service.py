from sqlalchemy.orm import Session
from smos.models.ecology import ValueAssessment
from typing import Dict, Any

class ValueService:
    def __init__(self, db: Session):
        self.db = db

    def assess_knowledge_value(self, node_id: int, human_benefit: float, environmental_impact: float):
        """Principle: Value requires human benefit"""
        knowledge_value = (human_benefit + (1.0 - environmental_impact)) / 2.0

        assessment = ValueAssessment(
            node_id=node_id,
            knowledge_value=knowledge_value,
            human_benefit=human_benefit,
            environmental_impact=environmental_impact,
            uncertainty=0.1
        )
        self.db.add(assessment)
        self.db.commit()
        self.db.refresh(assessment)
        return assessment

    def verify_human_meaning_principle(self, assessment_id: int):
        assessment = self.db.query(ValueAssessment).get(assessment_id)
        if assessment and assessment.human_benefit > 0.5:
            return True
        return False
