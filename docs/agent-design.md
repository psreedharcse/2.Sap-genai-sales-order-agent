# Entity Extraction Design

## Overview

Entity extraction converts natural language input into structured data required for SAP sales order operations.

---

## Key Entities

* customer_id
* amount
* sales_org
* distribution_channel
* division
* order_type
* payment_terms
* order_id

---

## Approach

### 1. LLM-Based Extraction

* Converts user query into structured JSON
* Uses prompt with predefined schema

### 2. Validation Layer

* Ensures required fields are present
* Converts data types (amount, quantity)

### 3. Mapping Layer

* Maps extracted entities to SAP OData payload

---

## Flow

User Query → LLM → JSON Entities → Validation → SAP Payload

---

## Benefits

* Structured input for SAP APIs
* Reduces manual data entry
* Improves automation accuracy
