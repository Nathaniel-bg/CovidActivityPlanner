
class venueInfo:
    def __init__(self):

        self.name = None
        self.address = None

        # Current time at the venue
        self.currentVenueTime = None
        # Gives a value from 0 to 200 percent for how busy the establishment is
        self.currentVenueStatus = None

    def live(self, liveData):
        self.currentVenueTime = liveData['venue_info']['venue_current_localtime']
        self.currentVenueStatus = liveData['analysis']['venue_live_busyness']

    def historical(self, historicalData):
        pass

    def basicInfo(self, name, address):
        self.name = name
        self.address = address

