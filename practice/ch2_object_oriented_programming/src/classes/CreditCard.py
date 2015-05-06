class CreditCard:
    """a consumer credit card"""
    def __init__(self, customer, bank, acnt, limit):
        """create a new credit card instance.
        The initial balance is 0.
        customer: name of the customer
        bank: name of the bank
        acont: acount identifier
        limit: credit limit
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """return name of the customer"""
        return self._customer

    def get_bank(self):
        """return the bank name"""
        return self._bank

    def get_account(self):
        """return card identifying number"""
        return self._account

    def get_limit(self):
        """return current credit limit"""
        return self._limit

    def get_balance(self):
        """return current balance"""
        return self._balance

    def charge(self,price):
        """charges to the crdit card
        True if charge was processed
        False if charge was denied"""
        if not isinstance(price,(int,float)):
            raise TypeError('price must be a number (int or float).')
        if price + self._balance>self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self,amount):
        """process customer payment that reduces balance"""
        self._balance -= amount

class PredatoryCreditCard(CreditCard):
    """an extension to CreditCard class that compounds interests and fees"""
    # how to do inheritance

    def __init__(self, customer, bank, acnt, limit, apr):
        """create a new predatory credit card instance
        apr: annual percentage rate (e.g., 0.0825 for 8.25% apr)"""
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        """charge given price to the card,
        assuming sufficient credit limit.
        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied"""
        success = super().charge(price)  # charge(price) return True or False
        if not success:
            self._balance += 5
        return success

    def process_month(self):
        """assess monthly interest on outstanding balance"""
        if self._balance > 0:
            # if positive balance, convert apr to monthly multiplicative factor
            monthly_factor = pow(1+self._apr, 1/12)
            self._balance *= monthly_factor








