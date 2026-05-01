from src.nlp_service import extract_entities
from src.tools import create_sales_order_tool, get_sales_order_status_tool

def select_tool(query: str) -> str:
    tool = call_llm_tool_selector(query)  # returns tool name
    return tool.strip()


def handle_request(query: str):
    tool = select_tool(query)
    entities = extract_entities(query)

    if tool == "create_sales_order":
        return create_sales_order_tool(entities)

    elif tool == "get_sales_order_status":
        return get_sales_order_status_tool(entities)

    return {"error": "No valid tool selected"}
