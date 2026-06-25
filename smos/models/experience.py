from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON, Float
from sqlalchemy.sql import func
from smos.core.database import Base

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String, nullable=True)
    author_id = Column(Integer, ForeignKey("cosmonauts.id"))
    contributors = Column(JSON, default=[])
    problem_type = Column(String)
    steps = Column(JSON, default=[])
    prerequisites = Column(JSON, default=[])
    resources = Column(JSON, default=[])
    outcome = Column(String, nullable=True)
    confidence = Column(Float, default=1.0)
    success_rate = Column(Float, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Reconstruction(Base):
    __tablename__ = "reconstructions"
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=True)
    evidence = Column(JSON, default=[])
    inferred_facts = Column(JSON, default=[])
    confidence = Column(Float, default=0.0)
    alternative_hypotheses = Column(JSON, default=[])
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class CausalRelation(Base):
    __tablename__ = "causal_relations"
    id = Column(Integer, primary_key=True, index=True)
    cause_node_id = Column(Integer, ForeignKey("memory_nodes.id"))
    effect_node_id = Column(Integer, ForeignKey("memory_nodes.id"))
    confidence = Column(Float, default=1.0)
    evidence = Column(JSON, default=[])
