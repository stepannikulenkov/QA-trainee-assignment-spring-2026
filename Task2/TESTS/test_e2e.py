import pytest
import random

def test_full_life_cycle(api_client, new_item):

    payload, item_id, sellerID = new_item

    response_get = api_client.get_item(item_id)
    assert response_get.status_code == 200 

    item_data = response_get.json()[0]
    assert item_data["name"] == payload["name"]
    assert item_data["price"] == payload["price"]
    assert item_data["sellerId"] == payload["sellerID"]

    response_stats = api_client.get_statistics(item_id)
    assert response_stats.status_code == 200
    stats_data = response_stats.json()[0]

    for key in ["likes", "viewCount", "contacts"]:
        assert stats_data[key] == payload["statistics"][key]

    response_delete = api_client.delete_item(item_id)
    assert response_delete.status_code == 200

    response_get_after_delete = api_client.get_item(item_id)
    assert response_get_after_delete.status_code == 404

    response_stats_after_delete = api_client.get_statistics(item_id)
    assert response_stats_after_delete.status_code == 404

