# SAP OData Integration with CSRF Handling

## Overview

This module integrates with SAP S/4HANA OData services to create and retrieve sales orders.

---

## CSRF Token Flow

1. Send GET request with header:
   x-csrf-token: Fetch

2. Receive token from response header

3. Use token in POST request

---

## API Operations

### Create Sales Order (POST)

* Uses CSRF token
* Sends JSON payload

### Get Sales Order Status (GET)

* Retrieves order details

---

## Flow

FastAPI → Agent → SAP Service → OData API → Response

---

## Benefits

* Secure SAP interaction
* Prevents unauthorized changes
* Ensures compliance with SAP Gateway
