from src.sap_service import create_sales_order, get_sales_order_status

def create_sales_order_tool(data):
    return create_sales_order(data)

def get_sales_order_status_tool(data):
    order_id = data.get("order_id")
    return get_sales_order_status(order_id)
