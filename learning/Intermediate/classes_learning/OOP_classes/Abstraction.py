# Abstraction
# Derived classes

from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def process_payment(self):
        pass


class CreditCardPayment(Payment):
    def process_payment(self):
        # Code to process Credit Card payment
        pass


class StripPayment(Payment):
    def process_payment(self):
        # Code to process Credit Card payment
        pass


class PayPalPayment(Payment):
    def process_payment(self):
        # Code to process Credit Card payment
        pass
