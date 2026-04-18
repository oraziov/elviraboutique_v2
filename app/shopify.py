import requests
from app.config import SHOP, TOKEN, API_VERSION

URL = f"https://{SHOP}/admin/api/{API_VERSION}/graphql.json"

HEADERS = {
    "X-Shopify-Access-Token": TOKEN,
    "Content-Type": "application/json"
}

def graphql(query, variables=None):
    res = requests.post(
        URL,
        json={"query": query, "variables": variables},
        headers=HEADERS
    )
    return res.json()
