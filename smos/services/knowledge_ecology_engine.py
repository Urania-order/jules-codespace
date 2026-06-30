from sqlalchemy.orm import Session
from smos.models.models import MemoryNode, KnowledgeLifecycleState
from smos.models.epistemic import IntellectualCluster
from smos.models.ecology import KnowledgeActivation
from typing import List
from datetime import datetime, timezone

class KnowledgeEcologyEngine:
    def __init__(self, db: Session):
        self.db = db

    def propagate_knowledge(self, node_id: int):
        """Propagate knowledge through resonance and cluster interaction"""
        node = self.db.query(MemoryNode).get(node_id)
        if not node:
            return

        # Increase cluster resonance
        for cluster_id in node.cluster_ids:
            cluster = self.db.query(IntellectualCluster).get(cluster_id)
            if cluster:
                cluster.knowledge_inflow += 0.1
                cluster.resonance = min(1.0, cluster.resonance + 0.05)
                cluster.activity = min(1.0, cluster.activity + 0.1)

        self.db.commit()

    def activate_resonance(self, node_id: int):
        """Increase resonance based on successful application/experiment"""
        activation = self.db.query(KnowledgeActivation).filter(KnowledgeActivation.node_id == node_id).first()
        if activation:
            activation.usage_count += 1
            activation.last_reinforced_at = datetime.now(timezone.utc)
            self.db.commit()

    def manage_dormancy(self):
        """Identify knowledge nodes that have low resonance and should enter dormancy"""
        # Logic to flag nodes as dormant if last_reinforced_at is old
        pass
