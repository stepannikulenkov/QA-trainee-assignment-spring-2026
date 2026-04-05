import pytest

def test_get_item_by_id(api_client, new_item):

    item_id = new_item[1]

    response = api_client.get_item(item_id)

    assert response.status_code == 200 

def test_check_keys(api_client, new_item):

    payload, item_id, sellerID = new_item

    response = api_client.get_item(item_id)

    assert response.status_code == 200

    response = response.json()[0]

    payload_stat = payload["statistics"]
    response_stat = response["statistics"]  

    assert item_id == response["id"]
    assert sellerID == response["sellerId"]
    assert payload["name"] == response["name"]
    assert payload["price"] == response["price"]

    assert payload_stat["likes"] == response_stat["likes"]
    assert payload_stat["viewCount"] == response_stat["viewCount"]
    assert payload_stat["contacts"] == response_stat["contacts"]

def test_content_type(api_client, new_item):

    payload, item_id, sellerID = new_item

    response = api_client.get_item(item_id)
    assert response.status_code == 200

    data = response.json()
    assert "application/json" in response.headers.get("Content-Type", "")

def test_createdAt(api_client, new_item):

    payload, item_id, sellerID = new_item

    response = api_client.get_item(item_id)
    assert response.status_code == 200
    response = response.json()[0]
    assert "createdAt" in response 

@pytest.mark.parametrize("item_id", [14231231, -121231, None])
def test_id_negative(api_client, item_id):

    response = api_client.get_item(item_id)
    assert response.status_code in [400, 404, 405]
    

    
