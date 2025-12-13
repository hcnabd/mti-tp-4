# Every time you add a new payment method, you have to modify the `PaymentProcessor` class to add another `elif` branch. This violates the Open/Closed Principle (OCP) because the class is not closed for modification—changes require editing existing code, which can introduce bugs.

# ------------------------------------------------------------

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} with credit card")

class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} with PayPal")

class BitcoinPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} with Bitcoin")

class PaymentProcessor:
    def process_payment(self, amount, method: PaymentMethod):
        method.pay(amount)

processor = PaymentProcessor()
processor.process_payment(100, CreditCardPayment())
processor.process_payment(50, PayPalPayment())
processor.process_payment(0.01, BitcoinPayment())
