# JSON Mapping Design (NLP → SAP OData)

## Overview

This layer transforms extracted entities from natural language into SAP-compliant OData payloads.

---

## Input

Structured JSON from NLP layer containing business entities.

---

## Output

SAP OData payload required for creating or retrieving sales orders.

---

## Mapping Logic

| NLP Field            | SAP Field            |
| -------------------- | -------------------- |
| customer_id          | SoldToParty          |
| sales_org            | SalesOrganization    |
| distribution_channel | DistributionChannel  |
| division             | OrganizationDivision |
| order_type           | SalesOrderType       |
| payment_terms        | PaymentTerms         |

---

## Flow

Entities JSON → Mapping → SAP Payload → API Execution

---

## Benefits

* Ensures SAP-compliant requests
* Decouples NLP from SAP logic
* Enables dynamic API execution
