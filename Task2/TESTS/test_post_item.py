import requests

def test_item_data(api_client, new_item): #проверка на совпадение данных с отправленными
    item_id = new_item[1]
    payload = new_item[0]

    response = api_client.get_item(item_id)
    assert response.status_code == 200

    data = response.json()[0]

    assert data["id"] == item_id
    assert data["name"] == payload["name"]
    assert data["price"] == payload["price"]
    assert data["sellerId"] == payload["sellerID"]
    assert data["statistics"] == payload["statistics"]

def test_item_in_statistics(api_client, new_item):

    sellerID = new_item[2]
    item_id = (new_item[1])

    response = api_client.get_statistics(sellerID)
    assert response.status_code == 200

    data = response.json()

    print(response.json())
    assert any(x["id"] == (item_id) for x in data)
    assert any(x["sellerId"] == (sellerID) for x in data)

    
    
