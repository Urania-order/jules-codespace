from sqlalchemy.orm import Session
from smos.models.ecology import TranslatedMessage
from typing import Dict, Any, List

class TranslatorService:
    def __init__(self, db: Session):
        self.db = db

    def translate_message(self, source_id: int, target_profile_id: int, content: str):
        # In a real system, LLM would analyze profiles and rewrite
        rewrite = f"Translated for profile {target_profile_id}: {content}"

        translated = TranslatedMessage(
            original_content=content,
            interpreted_meaning="Seeking collaboration",
            suggested_rewrite=rewrite,
            source_cosmonaut_id=source_id,
            target_behavior_profile_id=target_profile_id,
            risk_of_conflict=0.1
        )
        self.db.add(translated)
        self.db.commit()
        self.db.refresh(translated)
        return translated

    def mediate_conflict(self, message_a: str, message_b: str):
        return {
            "neutral_ground": "Both parties value productivity but have different speeds.",
            "suggested_compromise": "User A provides quick drafts, User B performs deep review weekly."
        }

    def explain_intent(self, message_content: str, author_id: int):
        """Explain the underlying intent of a message to reduce misunderstanding"""
        # In v0.8, this would be LLM-driven
        return {
            "original": message_content,
            "inferred_intent": "The author is seeking critical feedback to improve the quality, not criticizing the recipient.",
            "suggested_response_style": "Constructive and detailed."
        }

    def de_escalate(self, interaction_history: List[str]):
        """Identify rising tension and suggest de-escalation strategies"""
        return {
            "tension_level": "MODERATE",
            "observation": "Direct language is being interpreted as hostile.",
            "advice": "Switch to asynchronous communication for 24 hours to allow for reflection."
        }
