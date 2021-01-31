
import requests
import json
import TestConstants as con
import venue as v

def obtainHistoryData(venue):
    url = "https://besttime.app/api/v1/forecasts"

    # Parameters used to communicate with API
    params = {
        'api_key_private': con.BestTimeInfo.Api_Key_Private,
        'venue_name': venue.name,
        'venue_address': venue.address
    }

    response = requests.request("POST", url, params=params)
    data = json.loads(response.text)

    if not (data['status'] == 'Error'):
        # venueInfo = v.venueInfo()
        venue.addHistorical(data)