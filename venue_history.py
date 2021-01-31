class VenueHistory:
  def __init__(self, historyData):
    self.historyData = historyData

  def getRawDayData(self, day):
    print("Hello my name is ")

    if(day == 'Monday'):
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