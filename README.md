# SAP GenAI Sales Order Agent

## Overview

This project implements an AI-driven SAP sales order automation system that converts natural language input into SAP S/4HANA OData operations using LLM, agent-based orchestration, and FastAPI.

---

# Business Problem

Business users cannot directly interact with SAP systems using natural language, leading to manual effort, dependency on technical teams, and slower sales order processing.

---

# Solution

Designed an intelligent AI agent that:

* Understands natural language input
* Extracts intent and business entities
* Dynamically selects SAP APIs
* Generates SAP-compliant OData payloads
* Executes transactions securely in SAP S/4HANA

---

# Key Features

* LLM-based intent classification
* Entity extraction using structured JSON
* Agent-based dynamic tool selection
* SAP OData integration
* CSRF token handling
* FastAPI orchestration layer
* Retry and fallback mechanisms

---

# Architecture

User → FastAPI → Agent → NLP → Entity Extraction → Mapping → SAP OData → Response

---

# Tech Stack

* Python
* FastAPI
* SAP S/4HANA OData APIs
* OpenAI / SAP GenAI Hub
* JSON Mapping
* REST APIs

---

# Supported Operations

## Create Sales Order

Converts natural language into SAP sales order creation requests.

---

## Get Sales Order Status

Retrieves SAP sales order details dynamically.

---

# Example User Queries

* “Create a sales order for customer 25100273 with amount 300 EUR”
* “Check status of sales order 107”

---

# Security

* CSRF token handling
* SAP authentication
* Validation before execution

---

# Error Handling

* Validation checks
* Retry mechanisms
* Token refresh handling
* Graceful fallback responses

---

# Scalability

* Stateless FastAPI services
* Horizontal scaling support
* Modular architecture for additional tools

---

# Future Enhancements

* Multi-agent orchestration
* Human-in-the-loop approval
* RAG integration
* Multi-channel integration (Teams / Outlook)

