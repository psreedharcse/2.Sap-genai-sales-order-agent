# Intent Classification Design

## Overview

The system classifies user queries into predefined intents to determine the correct business action.

---

## Supported Intents

* CreateOrder
* GetStatus

---

## Approach

### 1. Rule-Based Classification

* Fast and deterministic
* Handles common patterns

### 2. LLM-Based Classification

* Handles flexible natural language
* Used when rules do not match

---

## Benefits

* High accuracy
* Low latency for common queries
* Reliable fallback mechanism
