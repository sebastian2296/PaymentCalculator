class Shift:
    """
    A class representing a work shift.
    """
    def __init__(self, day: str, start: str, end: str) -> None:
        self.day = day
        self.start_hour, self.start_minute = map(int, start.split(":"))
        self.end_hour, self.end_minute = map(int, end.split(":"))

    def duration(self):
        """
        Calculates the duration of the shift in hours.
        Returns:
            The duration of the shift in hours (float).
        """
        start = (self.start_hour + self.start_minute) / 60
        end = (self.end_hour + self.end_minute) / 60
        return end - start
