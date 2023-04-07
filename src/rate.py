from src.shift import Shift


class Rate:
    """
    A class representing a pay rate for a particular day and time range.
    """
    def __init__(self, day, start, end, rate) -> None:
        self.day = day
        self.start = start
        self.end = end
        self.rate = rate

    def is_same_day(self, shift: Shift) -> bool:
        """
        Determines if a given Shift object falls within the day and time range of this Rate object.
        Args:
            shift (Shift): the Shift object to check against this Rate object
        Returns:
            True if the Shift object falls within this Rate object's day and time range, False otherwise.
        """
        return (
            shift.day == self.day
            and shift.start_hour < self.end
            and shift.end_hour > self.start
        )

    def overlap_duration(self, shift: Shift) -> float:
        """
        Calculates the amount of time in hours that a given Shift object overlaps with this Rate object.
        Args:
            shift (Shift): the Shift object to calculate the overlap with
        Returns:
            The amount of time in hours that the Shift object overlaps with this Rate object (float).
        """

        overlap_start = max(self.start, shift.start_hour)
        overlap_end = min(self.end, shift.end_hour)
        return max(overlap_end - overlap_start, 0)
