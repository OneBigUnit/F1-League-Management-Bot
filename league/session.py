from typing import List

from .track import Track
from league import Driver


class Session:
    def __init__(self, track: Track, drivers: List[Driver]) -> None:
        self.track = track
        self.drivers = drivers
