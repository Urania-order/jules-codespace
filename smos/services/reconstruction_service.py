from sqlalchemy.orm import Session
from smos.models.experience import Reconstruction, CausalRelation
from typing import List, Dict, Any

class ReconstructionService:
    def __init__(self, db: Session):
        self.db = db

    def reconstruct_event(self, evidence: List[Dict[str, Any]], confidence: float):
        reconstruction = Reconstruction(
            evidence=evidence,
            confidence=confidence,
            inferred_facts={"status": "reconstructed", "reasoning": "Based on event log and causal graph"}
        )
        self.db.add(reconstruction)
        self.db.commit()
        self.db.refresh(reconstruction)
        return reconstruction

    def add_causal_relation(self, cause_id: int, effect_id: int, confidence: float):
        relation = CausalRelation(
            cause_node_id=cause_id,
            effect_node_id=effect_id,
            confidence=confidence
        )
        self.db.add(relation)
        self.db.commit()
        return relation
