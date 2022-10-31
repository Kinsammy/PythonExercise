class Account:

    def __init__(self, name, balanece):
        self._name = name

        if balanece > 0.0:
            self._balance = balanece

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def deposit(self, deposit_amount):
        if deposit_amount > 0.0:
            self._balance += deposit_amount

    def getBalance(self):
        return self._balance

    def withdraw(self, withdraw_amount):
        if self._balance > withdraw_amount:
            self._balance -= withdraw_amount

    def details(self):
        return "Account name: "+self.getName() + " " + " Account balance: "+str(self.getBalance())

