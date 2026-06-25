from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON, Float, Boolean
from sqlalchemy.sql import func
from smos.core.database import Base

class KnowledgeImpact(Base):
    __tablename__ = "knowledge_impacts"
    id = Column(Integer, primary_key=True, index=True)
    source_node_id = Column(Integer, ForeignKey("memory_nodes.id"))
    target_domain = Column(String)
    influence_type = Column(String) # DIRECT_INFLUENCE, INDIRECT_INFLUENCE, BEHAVIORAL_SHIFT, etc.
    confidence = Column(Float, default=0.0)
    cascade_depth = Column(Integer, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class KnowledgeActivation(Base):
    __tablename__ = "knowledge_activations"
    id = Column(Integer, primary_key=True, index=True)
    node_id = Column(Integer, ForeignKey("memory_nodes.id"))
    usage_count = Column(Integer, default=0)
    real_world_application = Column(JSON, default=[])
    decay_rate = Column(Float, default=0.01)
    last_reinforced_at = Column(DateTime(timezone=True), server_default=func.now())

class TranslatedMessage(Base):
    __tablename__ = "translated_messages"
    id = Column(Integer, primary_key=True, index=True)
    original_content = Column(String)
    interpreted_meaning = Column(String)
    suggested_rewrite = Column(String)
    emotional_weight = Column(Float, default=0.0)
    risk_of_conflict = Column(Float, default=0.0)
    source_cosmonaut_id = Column(Integer, ForeignKey("cosmonauts.id"))
    target_behavior_profile_id = Column(Integer, ForeignKey("behavior_profiles.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
