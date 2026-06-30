# ECO Co-SMOS Architecture

## System Design

ECO Co-SMOS is built as a modular ecosystem of services interacting with a central semantic and relational database (PostgreSQL with `pgvector`).

### Core Subsystems

1.  **Knowledge Ecology Engine (`smos/services/knowledge_ecology_engine.py`)**
    - The orchestrator of the knowledge lifecycle. It manages how nodes move between states (Idea -> Recipe -> Practice).
2.  **Value Physics Engine (`smos/services/value_physics_engine.py`)**
    - Calculates dynamic metrics for every knowledge object. Unlike traditional scoring, these values (Momentum, Potential, Entropy) are recalculated based on interaction and impact.
3.  **Attention Ecology Service (`smos/services/attention_ecology_service.py`)**
    - A recommendation layer focused on utility and "low-resonance" gems—valuable knowledge that hasn't yet reached its potential audience.
4.  **Resonance & Discovery (`smos/services/discovery_service.py`, `smos/services/ecology_service.py`)**
    - Implements semantic similarity, analogy detection, and backward discovery (reverse causal search).
5.  **Behavioral Collaboration Layer (`smos/services/translator_service.py`, `smos/services/twin_service.py`)**
    - Manages `Cosmonaut` profiles (Humans and AI) and facilitates cooperation through translation of cognitive styles.

## Data Model

- **MemoryNode:** The atomic unit of knowledge, featuring `lifecycle_state` and `epistemic_status`.
- **IntellectualCluster:** A living group of nodes and cosmonauts with its own health and diversity metrics.
- **Relation:** Directed edges defining the connections (CAUSES, SOLVES, INSPIRED_BY).
- **Timeline:** Supports parallel realities (REAL, SIMULATION, COUNTERFACTUAL) for experimentation.

## Technology Stack

- **Backend:** FastAPI (Python 3.12)
- **Database:** PostgreSQL + pgvector
- **Graph Logic:** NetworkX / Custom SQL
- **Communication:** MCP (Model Context Protocol) for AI agent integration.
