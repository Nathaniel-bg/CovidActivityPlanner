# Processing API Data from https://besttime.app/

import requests
import json
import TestConstants as con

# Following URL gives a POST for ALL the JSON on the forecast
# url = "https://besttime.app/api/v1/forecasts"

url = "https://besttime.app/api/v1/forecasts/live"

params = {
    'api_key_private': con.BestTimeInfo.Api_Key_Private,
    'venue_name': con.venueInfo.venueName,
    'venue_address': con.venueInfo.venueAddress
}

response = requests.request("POST", url, params=params)
data = json.loads(response.text)

print(data)









