class Booking:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def book(self):
        print(f"Booking {self.name} for {self.date}")


class Reservation:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def reserve(self):
        print(f"Reserving {self.name} for {self.date}")

        
def calculate_price(quantity, price):
    return quantity * price


def calculate_discounted_price(quantity, price, discount):
    discounted_price = price - (price * discount)
    return quantity * discounted_price
