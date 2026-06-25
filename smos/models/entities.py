from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON, Float
from sqlalchemy.sql import func
from smos.core.database import Base

class DigitalTwin(Base):
    __tablename__ = "digital_twins"
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    goals = Column(JSON, default=[])
    preferences = Column(JSON, default={})
    knowledge_base = Column(JSON, default={}) # Pointers or summary
    permissions = Column(JSON, default={})
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Cosmonaut(Base):
    __tablename__ = "cosmonauts"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String) # HUMAN, LLM, AGENT, DIGITAL_TWIN, SIMULATION, HISTORIAN, RECONSTRUCTOR
    name = Column(String)
    reputation_score = Column(Float, default=0.0)
    expertise = Column(JSON, default=[])
    successful_recipes_count = Column(Integer, default=0)
    failed_recipes_count = Column(Integer, default=0)

class Constellation(Base):
    __tablename__ = "constellations"
    id = Column(Integer, primary_key=True, index=True)
    mission = Column(String)
    members = Column(JSON, default=[]) # List of cosmonaut IDs
    recipes = Column(JSON, default=[]) # Shared recipes
    reputation_score = Column(Float, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
