import pytest
import requests
from utils.api_client import ApiClient


@pytest.fixture
def api_client():
    return ApiClient()


@pytest.fixture
def new_item(api_client, request):
    sellerID = getattr(request, "param", 145535)

    payload = {
        "sellerID": sellerID,
        "name": "wqdf",
        "price": 121,
        "statistics": {
            "likes": 1542,
            "viewCount": 8765,
            "contacts": 231
        }
    }

    response = api_client.create_item(payload)
    assert response.status_code == 200

    status_str = response.json()["status"]
    item_id = status_str.split()[-1]

    return [payload, item_id, sellerID]
