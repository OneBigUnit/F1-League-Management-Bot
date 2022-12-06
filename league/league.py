from typing import Optional, List

from .track import Track
from . import Constructor, Driver


class League:
    DEFAULT_DESCRIPTION = ""
    DEFAULT_LOGO = "https://tonimarino.co.uk/wp-content/uploads/2019/08/f1-logo.png"

    def __init__(self, name: str, description: Optional[str] = None, logo: Optional[str] = None) -> None:
        self.name = name
        self.description = self.__class__.DEFAULT_DESCRIPTION if description is None else description
        self.logo = self.__class__.DEFAULT_LOGO if logo is None else logo
        self.constructors: List[Constructor] = []
        self.drivers: List[Driver] = []
        self.tracks: List[Track] = []

    def add_drivers(self, *drivers: Driver) -> None:
        for driver in drivers:
            self.drivers.append(driver)

    def add_tracks(self, *tracks: Track) -> None:
        for track in tracks:
            self.tracks.append(track)

    def add_constructors(self, *constructors: Constructor) -> None:
        for team in constructors:
            self.constructors.append(team)
