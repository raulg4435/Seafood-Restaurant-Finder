import config #
import requests 
import json 

def get_businesses( city ):

    headers = { "Authorization": f"Bearer {config.YELP_AUTH_TOKEN}" }
    params = {"location": city, "limit": 5, "term": "seafood"}

    request = requests.get(
        "https://api.yelp.com/v3/businesses/search",
        params=params,  
        headers=headers, 
    )

    return json.loads(request.text)["businesses"]
