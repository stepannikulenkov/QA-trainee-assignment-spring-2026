import requests

baseUrl = "https://qa-internship.avito.com"

class ApiClient:
    def create_item(self, payload):

        print("Payload:", payload)

        return requests.post(f"{baseUrl}/api/1/item", json = payload)
    
    def get_item(self, item_id):

        return requests.get(f"{baseUrl}/api/1/item/{item_id}")
    
    def get_statistics(self, sellerID):

        return requests.get(f"{baseUrl}/api/1/{sellerID}/item")
        