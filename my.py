class Bank_Account:

    def __init__(self, balance):
        self.__balance = balance    
        

    @property
    def balance(self):
        print(self.__balance)

    @balance.setter
    def balance(self, new_balance):
        if not isinstance(new_balance, (int, float)):
            print('Ошибка Валидации')
            return
        if new_balance < 0:
            print('Баланс меньше нуля')
            return 
        self.__balance = new_balance
        return 'Баланс обновлен'

person = Bank_Account(1000)
person.balance
person.balance = 2000
person.balance