from . import Driver


class Laptime:
    def __init__(self, minutes: int, seconds: int, milliseconds: int, driver: Driver):
        self.minutes = minutes
        self.seconds = seconds
        self.milliseconds = milliseconds
        self.driver = driver

    def __str__(self) -> str:
        return f"{self.minutes}:{self.seconds:02}.{self.milliseconds:03} - {self.driver}"
