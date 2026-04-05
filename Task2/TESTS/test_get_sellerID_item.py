import pytest
import random  

def test_get_items_by_seller_id(api_client, new_item):

    payload, item_id, sellerID = new_item

    payload_1 = {
  "sellerID": sellerID ,
  "name": "Сwfwf",
  "price": 121,
  "statistics": {
    "likes": 1542,
    "viewCount": 8765,
    "contacts": 231
  }
}
    response_1 = api_client.create_item(payload_1)
    response = api_client.get_seller_items(sellerID)

    assert response.status_code == 200 
    assert response_1.status_code == 200 

    data = response.json()


    assert isinstance(data, list)
    assert len(data) > 1

    for item in data:
        assert item["sellerId"] == sellerID
        assert "id" in item
        assert "sellerId" in item
        assert "name" in item
        assert "price" in item
        assert "statistics" in item
        assert "createdAt" in item

def test_get_3_items(api_client, new_item):

    payload, item_id, sellerID = new_item

    payload_1 = {
  "sellerID": sellerID ,
  "name": "Iphone10",
  "price": 141,
  "statistics": {
    "likes": 1542,
    "viewCount": 8765,
    "contacts": 231
  }
}
    
    payload_2 = {
  "sellerID": sellerID ,
  "name": "Iphone11",
  "price": 1212331,
  "statistics": {
    "likes": 14542,
    "viewCount": 7,
    "contacts": 21
  }
}
    api_client.create_item(payload_1)
    api_client.create_item(payload_2)
    response = api_client.get_seller_items(sellerID)

    data = response.json()
    assert len(data) == 3
    for item in data:
        item["sellerId"] == sellerID

    content_type = response.headers.get("Content-Type", "")
    assert "application/json" in content_type

@pytest.mark.parametrize("sellerID", [None, "abc", -1 ])
def test_get_items_by_id_negative(api_client, sellerID):

    response = api_client.get_seller_items(sellerID)

    assert response.status_code in [400, 404]



    
        




    

