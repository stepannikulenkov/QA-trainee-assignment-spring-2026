import pytest

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

def test_item_in_statistics(api_client, new_item): #объявление в массиве статистики

    sellerID = new_item[2]
    item_id = new_item[1]
    payload = new_item[0]

    response = api_client.get_statistics(sellerID)
    assert response.status_code == 200

    data = response.json()

    assert any(x["id"] == (item_id) for x in data)
    assert any(x["sellerId"] == (sellerID) for x in data)
    assert any(x["name"] == (payload["name"]) for x in data)
    assert any(x["price"] == (payload["price"]) for x in data)
    assert any(x["statistics"] == (payload["statistics"]) for x in data)


@pytest.mark.parametrize(
    "sellerID",
    [111111, 999999],
)
def test__boarders(api_client, sellerID):

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
    response_post = api_client.create_item(payload)
    assert response_post.status_code == 200

    status_str = response_post.json()["status"]
    item_id = status_str.split()[-1]

    response = api_client.get_item(item_id)
    assert response.status_code == 200

    data = response.json()[0]
    assert data["sellerId"] == sellerID

def test_two_items_same_seller(api_client):
    sellerID = 185535

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

    response1 = api_client.create_item(payload)
    assert response1.status_code == 200
    item_id_1 = response1.json()["status"].split()[-1]

    response2 = api_client.create_item(payload)
    assert response2.status_code == 200
    item_id_2 = response2.json()["status"].split()[-1]

    response = api_client.get_statistics(sellerID)
    assert response.status_code == 200

    data = response.json()

    ids = [x["id"] for x in data]

    assert item_id_1 in ids
    assert item_id_2 in ids

@pytest.mark.parametrize("name", [None, ""])
def test_without_name(api_client, name):
    
    payload = {
        "sellerID": 185537,
        "name": name,
        "price": 121,
        "statistics": {
            "likes": 1542,
            "viewCount": 8765,
            "contacts": 231
        }
    }
    response = api_client.create_item(payload)
    assert response.status_code == 400
    print(response.json())

@pytest.mark.parametrize("sellerID", [None, "abc", 0 , -1])
def test_sellerID_negative(api_client, sellerID):
    
    payload = {
        "sellerID": sellerID,
        "name": "iphone",
        "price": 121,
        "statistics": {
            "likes": 1542,
            "viewCount": 8765,
            "contacts": 231
        }
    }
    response = api_client.create_item(payload)
    assert response.status_code == 400
    print(response.json())

@pytest.mark.parametrize("price", [None, -12345, "abc"])
def test_price_negative(api_client, price):
    
    payload = {
        "sellerID": 185537,
        "name": "iphone",
        "price": price,
        "statistics": {
            "likes": 1542,
            "viewCount": 8765,
            "contacts": 231
        }
    }
    response = api_client.create_item(payload)
    assert response.status_code == 400
    print(response.json())

def test_without_statistics(api_client):

    payload = {
        "sellerID": 185537,
        "name": "iphone",
        "price": 1000,
        "statistics": None
    }
     
    response = api_client.create_item(payload)
    assert response.status_code == 400 

def test_post_without_body(api_client):

    payload = {}

    response = api_client.create_item(payload)
    assert response.status_code == 400

def test_statistics_likes(api_client):
    
    payload = {
        "sellerID": 185537,
        "name": "iphone",
        "price": 1000,
        "statistics": {
            "likes": 0,
            "viewCount": 8765,
            "contacts": 231
        }
    }

    response = api_client.create_item(payload)
    assert response.status_code == 200 

def test_statistics_likes_negativ(api_client):
    
    payload = {
        "sellerID": 185537,
        "name": "iphone",
        "price": 1000,
        "statistics": {
            "likes": -1,
            "viewCount": 8765,
            "contacts": 231
        }
    }

    response = api_client.create_item(payload)
    assert response.status_code == 400 
    
def test_check_sellerID(api_client, new_item):

    payload, item_id, sellerID  = new_item
    response = api_client.get_item(item_id)
    data = response.json()[0]

    get_keys = set(data.keys())
    post_keys = set(payload.keys())

    print("keys only from GET:", get_keys - post_keys)
    print("keys only from POST:", post_keys - get_keys)

    assert data["sellerID"] == sellerID
