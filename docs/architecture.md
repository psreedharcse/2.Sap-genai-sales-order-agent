# Architecture Overview

User → LLM → Agent → API Layer → SAP S/4HANA → Response

* LLM handles intent and entity extraction
* Agent decides which operation to perform
* API layer executes SAP OData calls
* Response returned to user
