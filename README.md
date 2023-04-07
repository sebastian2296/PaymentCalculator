# Payment Calculator
This is a simple payment calculator that takes a work schedule (from a .txt file) and calculates the total payment for that schedule based on a set of rates.

## How to execute this code

- Clone this repository and run `python main.py` followed by the path of the .txt file you want to be parsed. For example, to run calculations for a file called `sample.txt` that is located in your current directory, you'll have to run: `python main.py sample.txt`. If no path is provided, the script uses a provided `sample.txt` file in the root of this repo.

- There's a test for the `calculate_shift_payment` method from the PaymentCalculator class. To execute it, run `python test.py`. This tests is, essentially, creating a payment calculation from this method and then checking it against what we know is the correct value.

## Architecture
The code is organized in several modules:

- `shift.py`: defines a Shift class that represents a work shift with a day, start time and end time.
- `rate.py`: defines a Rate class that represents a rate for a specific day and time range, and has a method to calculate the overlap duration with a shift.
- `payment_calculator.py`: defines a PaymentCalculator class that takes a list of rates and has a method to calculate the payment for a given work schedule.
- `main.py`: a command-line interface that uses the PaymentCalculator class to calculate the payment for a given work schedule.
- The `PaymentCalculator` class uses the Shift and Rate classes to calculate the payment for each shift in the schedule, by finding the rates that apply to the shift and calculating the overlap duration.

## SOLID principles
The code follows some of the SOLID principles. By structuring the code in the above way, we make sure that it follows some of the SOLID principles. Mainly:

- `Single Responsibility Principle`: each class has a single responsibility: Shift represents a shift, Rate represents a rate, and PaymentCalculator calculates the payment for a schedule.
- `Open/Closed`: the code is open for extension (e.g. adding new rates) but closed for modification (existing classes don't need to change).
- `Interface Segregation`: there are no interfaces in the code, but each class exposes only the methods that are relevant for its role.
- `Dependency Inversion`: PaymentCalculator depends on abstractions (Shift and Rate) and not on concrete implementations, so it's easy to change the behavior of the system by changing the implementations.