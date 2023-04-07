from typing import List
import re
from src.rate import Rate
from src.shift import Shift


class PaymentCalculator:
    """
    A class for calculating payment based on shift schedules and rates.
    Attributes:
        rates (List[Rate]): A list of Rate objects representing the hourly rates for each day and time range.
    """
    def __init__(self, rates: List[Rate]):
        self.rates = rates

    def calculate_payment(self, employee: str, schedule: str) -> float:
        """
         Calculates the total payment for a given employee based on their shift schedule and the rates.
            Args:
                employee (str): The name of the employee.
                schedule (str): A comma-separated string of shift times in the format "Day HH:MM-HH:MM".
            Returns:
                A string representing the total payment in USD.
        """
        shifts = self.parse_schedule(schedule)
        total_payment = sum(self.calculate_shift_payment(shift) for shift in shifts)
        return f"The amount to pay {employee} is: {total_payment} USD"

    def parse_schedule(self, schedule: str) -> List[Shift]:
        """
        Parses a string of shift times into a list of Shift objects.
        Args:
            schedule (str): A comma-separated string of shift times in the format "Day HH:MM-HH:MM".
        Returns:
            A list of Shift objects representing each shift.
        """
        shifts = []
        for shift_str in schedule.split(","):
            start_time, end_time = shift_str.split("-")
            day, start_time = re.split("([aA-Zz]+)", start_time)[1:]
            shift = Shift(day, start_time, end_time)
            shifts.append(shift)
        return shifts

    def calculate_shift_payment(self, shift: Shift) -> float:
        """
        Calculates the payment for a single shift based on the rates.
        Args:
            shift (Shift): A Shift object representing the shift.
        Returns:
            The payment for the shift in USD.
        """
        applicable_rates = [rate for rate in self.rates if rate.is_same_day(shift)]
        shift_payment = sum(
            rate.rate * rate.overlap_duration(shift) for rate in applicable_rates
        )
        return shift_payment
