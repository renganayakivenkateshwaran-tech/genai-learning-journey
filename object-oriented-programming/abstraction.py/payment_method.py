from abc import ABC,abstractmethod
class PaymentMethod:
    def __init__(self,method):
        self.method = method
    @abstractmethod
    def pay(self,amount):
        pass
    def show_method(self):
        print(f"Payment Method: {self.method}")
class payment(PaymentMethod):
    def process_payment(self,amount):
        print(f"Payment of ${amount} succesful")
upi = payment("UPI")
card = payment("Card")
upi.show_method()
upi.process_payment(500)
card.show_method()
card.process_payment(1200)