from src.nlp_service import classify_intent

def handle_request(query: str):
    intent = classify_intent(query)

    if intent == "CreateOrder":
        return create_order_flow(query)
    elif intent == "GetStatus":
        return get_status_flow(query)
    else:
        return {"error": "Unknown intent"}
