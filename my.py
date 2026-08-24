class Bank_Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Зачислено: {amount}')

    def get_balance(self):
        print(self.__balance)

person = Bank_Account('P', 1000)
person.deposite(500)
person.get_balance()
