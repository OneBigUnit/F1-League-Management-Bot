from typing import List

from .track import Track
from .session import Session
from . import Driver


class Qualifying(Session):
    def __init__(self, track: Track, drivers: List[Driver]) -> None:
        super().__init__(track, drivers)
