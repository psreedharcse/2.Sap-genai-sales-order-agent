def classify_intent(query: str) -> str:
    query_lower = query.lower()

    # Rule-based fallback (fast + reliable)
    if "create" in query_lower and "order" in query_lower:
        return "CreateOrder"
    if "status" in query_lower or "check" in query_lower:
        return "GetStatus"

    # LLM-based classification (pseudo)
    intent = call_llm(query)  # replace with actual API
    return intent.strip()
