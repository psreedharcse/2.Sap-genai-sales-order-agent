# Architecture Diagram – Sales Order GenAI System

## Overview

This architecture converts natural language input into SAP S/4HANA sales order operations using LLM, agent-based orchestration, and API execution.

---

## Architecture Layers

### 1. User Layer

Users interact via Teams, UI, or API.

---

### 2. NLP / LLM Layer

* Processes user input
* Extracts intent and entities
* Uses prompt templates

---

### 3. Agent Layer

* Decides action based on intent
* Maps user request to SAP operation

---

### 4. API Layer (FastAPI)

* Builds request payload
* Validates data
* Routes to SAP

---

### 5. SAP Integration Layer

* Handles OData API calls
* Manages CSRF tokens
* Handles authentication

---

### 6. SAP S/4HANA System

* Executes business operations
* Returns response

---

### 7. Response Layer

* Formats output
* Sends back to user

---

## Flow Summary

User → LLM → Agent → API → SAP → Response
