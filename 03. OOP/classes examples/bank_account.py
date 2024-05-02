class BankAccount(object):
    """
    A class representing a simple bank account.
    """

    def __init__(self, name: str, balance: float = 0.0):
        """
        Initializes a BankAccount instance with the provided name and balance.
        """
        self.name = name
        self.balance = balance

    def deposit(self, x: float) -> float:
        """
        Deposits the specified amount into the account and returns the updated balance.
        """
        self.balance += x
        return self.balance
    
    def withdrawal(self, x: float) -> float:
        """
        Withdraws the specified amount from the account if sufficient funds are available
        and returns the updated balance. Raises an error if there are insufficient funds.
        """
        if self.balance < x:
            raise ValueError("Not enough funds")
        else:
            self.balance -= x
            return self.balance
    
    def get_balance(self) -> float:
        """
        Retrieves the current balance of the account.
        """
        return round(self.balance, 3)
    
    def get_name(self) -> str:
        """
        Retrieves the name associated with the account.
        """
        return self.name

a = BankAccount('Julie', 100)
a.withdrawal(93.40)
print(a.get_balance())
