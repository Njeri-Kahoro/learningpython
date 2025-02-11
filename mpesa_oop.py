from abc import ABC, abstractmethod

#encapsulation
#1 Usage
class Account:

    def __init__(self, account_id, holder_name, balance):
        self.account_id = account_id
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print (f"Attempting to withdraw {amount} from account with balance" f"{self.balance}")

        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance

    def get_holder_name(self):
        return self.holder_name

#Inheritance

class Customer(Account):

    def __init__(self, account_id, holder_name, balance, phone_number):
        super(). __init__(account_id, holder_name, balance)
        self.phone_number = phone_number


#polymorphism

#1 Usage
class Transaction(ABC):
    def __init__(self, amount):
        self.amount = amount

    def execute(self, amount):
        pass

class DepositTransaction(Transaction):
    def execute(self, account):
        account.deposit(self.amount)


class WithdrawTransaction(Transaction):
    def execute(self, account):
        account.withdraw(self.amount)



#Abstraction
class PaymentSystem(Transaction):
    @abstractmethod
    def process_payment(self, amount):
        pass

class MpesaPaymentSystem(PaymentSystem):
    def process_payment(self, amount):
        print(f'Processing Mpesa payment of {amount}')




#example usage

mpesa = MpesaPaymentSystem()
account1 = Customer(1, 'Kahoro', 200,'719415406')

deposit = DepositTransaction(450)
withdraw = WithdrawTransaction(2180)


deposit.execute(account1)
withdraw.execute(account1)
print(f'The balance of {account1.holder_name()} is {account1.get_balance()}')



