import pytest
from utils.api_client import ApiClient


@pytest.fixture
def api_client():
    return ApiClient()


@pytest.fixture
def new_item(api_client):
    payload = {
  "sellerID": 145535 ,
  "name": "wqdf",
  "price": -121,
  "statistics": {
    "likes": 1542,
    "viewCount": 8765,
    "contacts": 231
  }
}

    response = api_client.create_item(payload)

    assert response.status_code == 200, f"Ошибка создания: {response.text}"

    status_str = response.json()["status"]
    item_id = status_str.split()[-1]

    sellerID = payload["sellerID"]

    return [payload, item_id, sellerID]
