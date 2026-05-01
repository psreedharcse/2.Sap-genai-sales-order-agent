# FastAPI Orchestration Layer

## Overview

FastAPI acts as the central orchestration layer connecting NLP processing, agent decision-making, and SAP API execution.

---

## Components

### 1. API Layer

* Receives user request
* Exposes REST endpoint

### 2. Agent Layer

* Determines intent
* Routes request

### 3. NLP Layer

* Extracts intent and entities

### 4. Mapping Layer

* Converts entities into SAP payload

### 5. SAP Layer

* Executes OData API

---

## Flow

User → FastAPI → Agent → NLP → Mapper → SAP → Response

---

## Benefits

* Modular architecture
* Easy integration with UI and channels
* Scalable API-based system
