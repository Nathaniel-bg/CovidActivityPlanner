# Processing API Data from https://besttime.app/

import requests
import json
import TestConstants as con
import venue as v

def liveData():
    # Following URL gives a POST for ALL the JSON on the live forecast
    url = "https://besttime.app/api/v1/forecasts/live"

    # Parameters used to communicate with API
    params = {
    'api_key_private': con.BestTimeInfo.Api_Key_Private,
    'venue_name': con.venueInfo.venueName,
    'venue_address': con.venueInfo.venueAddress
    }

    response = requests.request("POST", url, params=params)
    data = json.loads(response.text)

    venueInfo = v.venueLiveInfo(data)
    return venueInfo










