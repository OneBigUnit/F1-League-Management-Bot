class Track:
    def __init__(self, name: str, country: str, lap_distance: int) -> None:
        self.name = name
        self.country = country
        self.lap_distance = lap_distance

    def __str__(self) -> str:
        return self.name
