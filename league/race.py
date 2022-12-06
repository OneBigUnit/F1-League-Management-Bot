from typing import List

from .track import Track
from .session import Session
from . import Driver


class Race(Session):
    def __init__(self, track: Track, drivers: List[Driver], number_of_laps: int) -> None:
        super().__init__(track, drivers)
        self.number_of_laps = number_of_laps
