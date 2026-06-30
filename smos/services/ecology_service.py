from sqlalchemy.orm import Session
from smos.models.epistemic import IntellectualCluster, ClusterRelation
from smos.models.models import MemoryNode
from typing import List

class EcologyService:
    def __init__(self, db: Session):
        self.db = db

    def pollinate(self, source_cluster_id: int):
        """Find related clusters and suggest knowledge transfer"""
        relations = self.db.query(ClusterRelation).filter(
            ClusterRelation.source_cluster_id == source_cluster_id
        ).all()

        suggestions = []
        for rel in relations:
            suggestions.append({
                "target_cluster_id": rel.target_cluster_id,
                "action": "TRANSFER_PATTERNS",
                "reason": f"Active link via {rel.interaction_type}"
            })
        return suggestions

    def check_activation(self, cluster_id: int):
        cluster = self.db.query(IntellectualCluster).get(cluster_id)
        if not cluster:
            return False

        # Mock activation logic based on dormant topics
        if len(cluster.dormant_topics) > 0:
            return True
        return False

    def notify_ambassador(self, cluster_id: int, message: str):
        cluster = self.db.query(IntellectualCluster).get(cluster_id)
        if cluster and cluster.ambassador_id:
            print(f"Notifying Ambassador {cluster.ambassador_id} of cluster {cluster_id}: {message}")
            return True
        return False

    def trigger_resonance(self, source_node_id: int, target_cluster_id: int, strength: float, delay_days: int = 0):
        """Implement delayed and indirect effects on clusters"""
        # In v0.8, resonance affects cluster activity and health
        cluster = self.db.query(IntellectualCluster).get(target_cluster_id)
        if not cluster:
            return False

        # Apply impact (mocking delay by just recording it for now)
        cluster.activity += strength * 0.2
        cluster.resonance += strength

        if strength > 0.8:
            cluster.health += 0.05

        self.db.commit()
        return True
