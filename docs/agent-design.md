# Agent-Based Tool Execution

## Overview

The system uses an AI agent to dynamically select and execute tools (APIs) based on user queries.

---

## Tools

* create_sales_order
* get_sales_order_status

---

## Approach

### 1. Tool Selection

* LLM determines the appropriate tool

### 2. Entity Extraction

* Extract required parameters

### 3. Tool Execution

* Execute selected SAP API

---

## Flow

User → LLM → Tool Selection → Entity Extraction → Tool Execution → Response

---

## Benefits

* Flexible execution
* Scalable for adding new tools
* Reduces hardcoded logic
