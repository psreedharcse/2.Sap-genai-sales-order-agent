def build_sales_order_payload(entities: dict):
    return {
        "SalesOrderType": entities.get("order_type"),
        "SalesOrganization": entities.get("sales_org"),
        "DistributionChannel": entities.get("distribution_channel"),
        "OrganizationDivision": entities.get("division"),
        "SoldToParty": entities.get("customer_id")
    }
