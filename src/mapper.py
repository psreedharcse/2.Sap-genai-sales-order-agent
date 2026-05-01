def map_to_sap_payload(entities: dict) -> dict:
    return {
        "SalesOrderType": entities.get("order_type", "OR"),
        "SalesOrganization": entities.get("sales_org"),
        "DistributionChannel": entities.get("distribution_channel"),
        "OrganizationDivision": entities.get("division"),
        "SoldToParty": entities.get("customer_id"),
        "PaymentTerms": entities.get("payment_terms"),
        "to_Item": [
            {
                "Material": "PRODUCT_X",  # placeholder / can be dynamic
                "RequestedQuantity": "1"
            }
        ]
    }
