# ECO Co-SMOS Architecture

## Overview

ECO Co-SMOS is built on a modular architecture designed to support a living knowledge ecology.

## Core Subsystems

### 1. Knowledge Ecology Engine
Manages the lifecycle and propagation of knowledge objects.
- **Service**: `smos.services.ecology_service.py`
- **Models**: `smos.models.ecology.py`

### 2. Value Physics Engine
Calculates dynamic metrics for knowledge impact and health.
- **Service**: `smos.services.value_service.py`
- **Models**: `smos.models.ecology.py`

### 3. Attention Ecology Service
Recommends knowledge based on long-term value.
- **Service**: `smos.services.attention_service.py`

### 4. Behavioral Collaboration Layer
Manages user profiles and AI translation for cooperation.
- **Service**: `smos.services.translator_service.py`, `smos.services.coevolution_service.py`
- **Models**: `smos.models.cognitive.py`

### 5. Epistemic & Cluster Management
Handles the strict labeling of knowledge and the evolution of intellectual clusters.
- **Service**: `smos.services.epistemic_service.py`, `smos.services.discovery_service.py`
- **Models**: `smos.models.epistemic.py`

### 6. Research & Economy
Supports collective funding and reputation credits.
- **Service**: `smos.services.research_service.py`, `smos.services.economy_service.py`

## Data Layer
- **PostgreSQL + pgvector**: Primary storage for relational and semantic data.
- **SQLAlchemy**: ORM for database interactions.

## Interaction Layer
- **FastAPI**: REST API for external integrations and frontend.
- **MCP (Model Context Protocol)**: Exposes tools and resources to AI agents.
- **Agent Orchestrator**: Event-driven automation of system tasks.
