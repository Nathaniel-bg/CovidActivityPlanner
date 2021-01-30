
class venueLiveInfo:
    def __init__(self, liveData):
        # Current time at the venue
        self.currentVenueTime = liveData['venue_info']['venue_current_localtime']
        # Gives a value from 0 to 200 percent for how busy the establishment is
        self.currentVenueStatus = liveData['analysis']['venue_live_busyness']

