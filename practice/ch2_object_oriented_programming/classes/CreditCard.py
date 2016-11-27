class CreditCard:
    """a consumer credit card"""
    def __init__(self, customer, bank, acnt, limit, balance = 1):
        """create a new credit card instance.
        The initial balance is 0.
        customer: name of the customer
        bank: name of the bank
        acont: acount identifier
        limit: credit limit
        balance: nonzero balance using an optional parameter
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

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

    def _set_balance(self,b):
        self._balance = b
        return self._balance

    def charge(self,price):
        """charges to the crdit card
        True if charge was processed
        False if charge was denied"""
        if not isinstance(price,(int,float)):
            raise TypeError('price must be a number (int or float).')
        if price + self._balance > self._limit:
            return False
        else:
            #self._balance += price
            self._set_balance(self._balance+price)
            return True

    def make_payment(self,amount):
        """process customer payment that reduces balance"""
        if not isinstance(amount,(int, float)):
            raise TypeError('amount must be a number (int or float).')
        elif amount <= 0:
            raise ValueError('amount must be a positive number.')
        #self._balance -= amount
        self._set_balance(self._balance-amount)

class PredatoryCreditCard(CreditCard):
    """an extension to CreditCard class that compounds interests and fees"""
    # how to do inheritance

    def __init__(self, customer, bank, acnt, limit, balance, apr = 0, calls = 0, pay = 0):
        """create a new predatory credit card instance
        apr: annual percentage rate (e.g., 0.0825 for 8.25% apr)
        calls: how many calls (times) the customer has made to charge
        """
        super().__init__(customer, bank, acnt, limit, balance)
        self._apr = apr
        self._calls = calls
        self._pay = pay

    def charge(self, price):
        """charge given price to the card,
        assuming sufficient credit limit.
        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied"""
        success = super().charge(price)  # charge(price) return True or False

        if not success:
            #self._balance += 5
            self._set_balance(self._balance+5)
        elif success and self._calls > 10:
             # once a customer has made ten calls to charge in the current month,
             # each additional call to that function results in an additional $1 surcharge.
            #self._balance += 1
            self._set_balance(self._balance+1)
            self._calls += 1
        else:  # success
            self._calls += 1 #
        return success

    def process_month(self):
        """assess monthly interest on outstanding balance"""
        if self._balance > 0:
            # if positive balance, convert apr to monthly multiplicative factor
            monthly_factor = pow(1+self._apr, 1/12)
            #self._balance *= monthly_factor
            self._set_balance(self._balance*monthly_factor)

    def make_payment(self,amount):
        """
         a late fee is assessed if the customer does not subse-
         quently pay that minimum amount before the next monthly cycle
        :param amount:
        :return:
        """
        super().make_payment(amount)
        # minimum monthly payment
        mini_pay = 0.3 * self._balance
        if self._pay == 0  or amount < mini_pay:
            #self._balance += 5     # late fee
            self._set_balance(self._balance+5)












