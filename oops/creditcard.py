class CreditCard:
    """A class for credit card for consumer"""

    def __init__(self, bank, name, account, limit, initial_balance):
        """Create a new credit card instance"""
        
        self.bank = bank # public

        self._name = name # Non public member
        self._account = account
        self._limit = limit
        self._min_balance = 1000

        if initial_balance < self._min_balance:
            raise ValueError(f"Minimum Balance cannot be less than {self._min_balance}")
        self._balance = initial_balance 
        

    def get_bank_name(self):
        """ Return name of bank """
        return self.bank
    
    def get_customer_name(self):
        """ Return name of customer """
        return self._name
    
    def get_account_no(self):
        """ Return account number of customer """
        return self._account
    
    def get_limit(self):
        """Return account limit"""
        return self._limit
    
    def get_balance(self):
        """ Return bank balance """
        return self._balance
    
    def debit(self, amount):
        """ Debit an amount from credit card.
        Update the balance.
        Return True if transaction processed else return False denoting that transaction was denied. """

        if amount + self._balance > self._limit:
            return False
        else:
            self._balance -= amount
            return True

    def credit(self, amount):
        """ Credit/Recharge an amount in the credit card.
        Do not exceed the credit limit.
        Return the False if recharge exceeds limit else True. """

        if self._limit >= self._balance + amount:
            self._balance += amount
            return True
        else:
            return False
        


