from .constants import Severity
from datetime import datetime
from pytz import timezone


class Accident:
    _TIMEZONE = timezone('Asia/Jerusalem')

    def __init__(self, *, address, description, time, id_, longitude, latitude,
                 severity, title):
        self._address = address
        self._description = description
        self._time = time
        self._id = id_
        self._longitude = longitude
        self._latitude = latitude
        self._severity = severity
        self._title = title

    @property
    def address(self):
        return self._address

    @property
    def description(self):
        return self._description

    @property
    def time(self):
        return self._time

    @property
    def id(self):
        return self._id

    @property
    def longitude(self):
        return self._longitude

    @property
    def latitude(self):
        return self._latitude

    @property
    def severity(self):
        return self._severity

    @property
    def title(self):
        return self._title

    def __repr__(self):
        return "<Accident {}>".format(self._id)

    @classmethod
    def _parse_date(cls, time_string):
        try:
            time = datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            time = datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%S.%f")

        return cls._TIMEZONE.localize(time)

    @classmethod
    def from_json(cls, marker):
        return cls(title=marker['title'], description=marker.get('description'), address=marker.get('address'),
                   time=cls._parse_date(marker['created']),
                   id_=marker['id'], longitude=marker['longitude'], latitude=marker['latitude'],
                   severity=Severity(marker.get('severity', Severity.UNSPECIFIED)))
