import pytest 
import random

def test_get_statistic(api_client, new_item):

    payload, item_id, sellerID = new_item

    response = api_client.get_statistics(item_id)

    assert response.status_code == 200 

    data = response.json()

    for item in data:
        assert "likes" in item
        assert "viewCount" in item
        assert "contacts" in item
    
    assert isinstance(item["likes"], int)
    assert isinstance(item["viewCount"], int)
    assert isinstance(item["contacts"], int)

def test_item_content_type(api_client, new_item):

    payload, item_id, sellerID = new_item

    response = api_client.get_statistics(item_id)
    assert response.status_code == 200

    content_type = response.headers.get("Content-Type", "")
    assert "application/json" in content_type

def test_statistics_consistency_with_item(api_client, new_item):
    payload, item_id, sellerID = new_item

    response_item = api_client.get_item(item_id)
    assert response_item.status_code == 200
    item_data = response_item.json()[0]
    item_stats = item_data["statistics"]

    response_stats = api_client.get_statistics(item_id)
    assert response_stats.status_code == 200
    stats_data = response_stats.json()[0]

    for key in ["likes", "viewCount", "contacts"]:
        assert item_stats[key] == stats_data[key]
        assert isinstance(item_stats[key], int)
        assert isinstance(stats_data[key], int)

@pytest.mark.parametrize("item_id",[None, random.randint(0,999999), "abc"])
def test_get_statistics_negative(api_client, item_id):

    response = api_client.get_statistics(item_id)

    assert response.status_code in [400, 404, 405]

