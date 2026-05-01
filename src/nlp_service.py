import json

def validate_entities(entities):
    required_fields = ["customer_id", "sales_org"]

    for field in required_fields:
        if not entities.get(field):
            raise ValueError(f"Missing required field: {field}")

def extract_entities(query: str) -> dict:
    response = call_llm(query)  # LLM returns JSON

    try:
        entities = json.loads(response)
    except:
        return {}

    return normalize_entities(entities)


def normalize_entities(data: dict) -> dict:
    return {
        "customer_id": data.get("customer_id"),
        "amount": parse_amount(data.get("amount")),
        "sales_org": data.get("sales_org"),
        "distribution_channel": data.get("distribution_channel"),
        "division": data.get("division"),
        "order_type": data.get("order_type", "OR"),
        "payment_terms": data.get("payment_terms"),
        "order_id": data.get("order_id")
    }


def parse_amount(value):
    if not value:
        return None
    try:
        return float(value.split()[0])  # "300 EUR" → 300
    except:
        return None
