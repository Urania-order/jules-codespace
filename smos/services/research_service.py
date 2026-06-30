from sqlalchemy.orm import Session
from smos.models.ecology import ResearchPortal, ResearchSponsorship
from typing import List, Dict, Any

class ResearchService:
    def __init__(self, db: Session):
        self.db = db

    def open_portal(self, hypothesis_id: int):
        portal = ResearchPortal(hypothesis_id=hypothesis_id)
        self.db.add(portal)
        self.db.commit()
        self.db.refresh(portal)
        return portal

    def sponsor_research(self, portal_id: int, sponsor_id: int, amount: float):
        sponsorship = ResearchSponsorship(portal_id=portal_id, sponsor_id=sponsor_id, amount=amount)
        self.db.add(sponsorship)

        portal = self.db.query(ResearchPortal).get(portal_id)
        if portal:
            portal.budget += amount
            if portal.budget > 1000: # Mock funding threshold
                portal.status = "FUNDED"

        self.db.commit()
        self.db.refresh(sponsorship)
        return sponsorship

    def add_milestone(self, portal_id: int, description: str, target_outcome: str):
        """Add experimental milestone to research portal"""
        portal = self.db.query(ResearchPortal).get(portal_id)
        if not portal:
            return None

        outcomes = list(portal.outcomes)
        outcomes.append({
            "milestone": description,
            "target": target_outcome,
            "status": "PENDING"
        })
        portal.outcomes = outcomes
        self.db.commit()
        self.db.refresh(portal)
        return portal

    def verify_milestone(self, portal_id: int, milestone_index: int, proof_link: str):
        """Verify milestone achievement by community/participants"""
        portal = self.db.query(ResearchPortal).get(portal_id)
        if not portal or milestone_index >= len(portal.outcomes):
            return None

        outcomes = list(portal.outcomes)
        outcomes[milestone_index]["status"] = "VERIFIED"
        outcomes[milestone_index]["proof"] = proof_link
        portal.outcomes = outcomes
        self.db.commit()
        self.db.refresh(portal)
        return portal
