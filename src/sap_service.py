import requests

SAP_URL = "https://your-sap-system/sap/opu/odata/sap/API_SALES_ORDER_SRV"
USERNAME = "your_user"
PASSWORD = "your_password"

def fetch_csrf_token():
    headers = {
        "x-csrf-token": "Fetch"
    }

    response = requests.get(
        SAP_URL,
        headers=headers,
        auth=(USERNAME, PASSWORD)
    )

    token = response.headers.get("x-csrf-token")
    cookies = response.cookies

    return token, cookies


def create_sales_order(payload):
    token, cookies = fetch_csrf_token()

    headers = {
        "Content-Type": "application/json",
        "x-csrf-token": token
    }

    response = requests.post(
        f"{SAP_URL}/A_SalesOrder",
        json=payload,
        headers=headers,
        cookies=cookies,
        auth=(USERNAME, PASSWORD)
    )

    return response.json()


def get_sales_order_status(order_id):
    response = requests.get(
        f"{SAP_URL}/A_SalesOrder('{order_id}')",
        auth=(USERNAME, PASSWORD)
    )

    return response.json()

