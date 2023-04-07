from src.payment_calculator import PaymentCalculator
from src.rate import Rate
import logging
import argparse

# Initial list of rates
RATES = [
    Rate("MO", 0, 9, 25),
    Rate("MO", 9, 18, 15),
    Rate("MO", 18, 24, 20),
    Rate("TU", 0, 9, 25),
    Rate("TU", 9, 18, 15),
    Rate("TU", 18, 24, 20),
    Rate("WE", 0, 9, 25),
    Rate("WE", 9, 18, 15),
    Rate("WE", 18, 24, 20),
    Rate("TH", 0, 9, 25),
    Rate("TH", 9, 18, 15),
    Rate("TH", 18, 24, 20),
    Rate("FR", 0, 9, 25),
    Rate("FR", 9, 18, 15),
    Rate("FR", 18, 24, 20),
    Rate("SA", 0, 9, 30),
    Rate("SA", 9, 18, 20),
    Rate("SA", 18, 24, 25),
    Rate("SU", 0, 9, 30),
    Rate("SU", 9, 18, 20),
    Rate("SU", 9, 24, 25),
]


def run(file_name):
    logging.basicConfig(format="%(message)s", level=logging.DEBUG)
    with open(file_name, "r") as file:
        txt_file = file.readlines()
        txt_file = [line.strip() for line in txt_file]

    calculator = PaymentCalculator(RATES)

    for line in txt_file:
        employee, schedule = line.split("=")
        payment = calculator.calculate_payment(employee, schedule)
        logging.info(payment)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate employee payments')
    parser.add_argument('file_name', nargs='?', default='sample.txt', help='name of the file containing the employee schedule')
    args = parser.parse_args()

    run(args.file_name)
