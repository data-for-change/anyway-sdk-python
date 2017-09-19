from yarl import URL
from datetime import datetime
from requests import Session
from .location import get_location_bounding_box

class Anyway:
    def __init__(self, url='https://www.anyway.co.il'):
        self._url = URL(url)
        self._session = Session()

    @staticmethod
    def _format_date(dt):
        return int((dt - datetime(1970, 1, 1)).total_seconds())

    def get_accidents(self, *, location, distance_in_km=1):
        bounding_box = get_location_bounding_box(location=location, distance_in_km=distance_in_km)
        url = (self._url / 'markers').with_query(
            ne_lat=str(bounding_box.lat_max), ne_lng=str(bounding_box.lon_max),
            sw_lat=str(bounding_box.lat_min), sw_lng=str(bounding_box.lon_min),
            zoom=17, thin_markers='false', approx=1, accurate=1, show_markers=1, show_urban=3,
            show_intersection=3, show_lane=3, show_day=7, show_holiday=0,
            show_time=24, start_time=25, end_time=25, weather=0, road=0,
            start_date=self._format_date(datetime(2013, 1, 1)),
            end_date=self._format_date(datetime.today()),
            show_light=1, show_severe=1, show_fatal=1,
            seperation=0, surface=0, acc_type=0, controlmeasure=0, district=0, case_type=0)

        response = self._session.get(url)
        response.raise_for_status()
        return response.json()['markers']
