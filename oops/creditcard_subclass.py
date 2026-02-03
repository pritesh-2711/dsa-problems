from creditcard import CreditCard

class AdvancedCard(CreditCard):
    """ Additions : 
    1. If recharge / credit is over balance, take 2% penalty from over the limit amount.
    2. If denied for debit, add a penalty of 2%.
    3. If balance lower than minimum balance, add 1% penalty."""

    def __init__(self, bank, name, account, limit, initial_balance, interest_rate=0.02):
        super().__init__(bank, name, account, limit, initial_balance)
        self.interest = interest_rate

    def credit(self, amount):
        """ Credit/Recharge an amount in the credit card.
        Do not exceed the credit limit.
        Return the False if recharge exceeds limit else True. 
        If recharge / credit is over balance, take 2% penalty from over the limit amount.
        """
        if super().credit(amount):
            return f"Updated Balance : {super().get_balance()}"
        else:
            self._balance += amount
            interest_amt = (self._balance - self._limit)*self.interest
            self._balance -= interest_amt
            return f"Updated Balance : {super().get_balance()} \nafter a limit exceeded penalty of {interest_amt} applied."
        
    def debit(self, amount):
        """Debit an amount from credit card.
        Update the balance.
        If denied for debit, add a penalty of 2%.
        If balance lower than minimum balance, add 1% penalty.
        """
        if super().debit(amount):
            if super().get_balance() > self._min_balance:
                return f"Updated Balance : {super().get_balance()}"
            else:
                penalty_amt = self._min_balance * 0.01
                self._balance -= penalty_amt
                return f"Updated Balance : {super().get_balance()} \nafter a minimum balance penalty of {penalty_amt} applied."
        else:
            self._balance -= amount
            interest_amt = (self._balance - self._limit)*self.interest
            self._balance -= interest_amt
            return f"Updated Balance : {super().get_balance()} \nafter a limit exceeded penalty of {interest_amt} applied."           

