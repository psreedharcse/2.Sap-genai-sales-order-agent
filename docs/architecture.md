# Architecture Overview — SAP GenAI Sales Order Agent

## High-Level Flow

User → FastAPI → Agent → NLP → SAP Integration → Response

---

# Components

## 1. User Layer

* Teams
* Web UI
* API Consumers

---

## 2. FastAPI Orchestration Layer

* Receives requests
* Routes execution
* Manages workflows

---

## 3. NLP / LLM Layer

* Intent classification
* Entity extraction

---

## 4. Agent Layer

* Tool selection
* Dynamic execution

---

## 5. Mapping Layer

* Converts entities into SAP OData payload

---

## 6. SAP Integration Layer

* OData API execution
* CSRF token handling

---

## 7. Response Layer

* Formats API response
* Returns user-friendly output

---

# Key Design Principles

* Modular architecture
* Loose coupling
* Dynamic tool execution
* Scalable API-driven design
