
class venueInfo:
    def __init__(self):

        self.name = None
        self.address = None

        # Current time at the venue
        self.currentVenueTime = None
        # Gives a value from 0 to 200 percent for how busy the establishment is
        self.currentVenueStatus = None

    def addLive(self, liveData):
        self.currentVenueTime = liveData['venue_info']['venue_current_localtime']
        self.currentVenueStatus = liveData['analysis']['venue_live_busyness']

    def addHistorical(self, historyData):
        self.historyData = historyData

    def basicInfo(self, name, address):
        self.name = name
        self.address = address

    def getRawDayData(self, day):
        if (day == 'Monday'):
            return self.historyData['analysis'][0]['day_raw']
        elif (day == 'Tuesday'):
            return self.historyData['analysis'][1]['day_raw']
        elif (day == 'Wednesday'):
            return self.historyData['analysis'][2]['day_raw']
        elif (day == 'Thursday'):
            return self.historyData['analysis'][3]['day_raw']
        elif (day == 'Friday'):
            return self.historyData['analysis'][4]['day_raw']
        elif (day == 'Saturday'):
            return self.historyData['analysis'][5]['day_raw']
        elif (day == 'Sunday'):
            return self.historyData['analysis'][6]['day_raw']