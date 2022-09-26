# Python Banking App
while True:
    try:
        totle_value = int(input('Enter Your Amount: '))
        class Bank: 

            while True:
                user_input = input("Withdrawal (Type 'w') / Deposit (Type 'd')  ? :")
                if user_input == 'w' or user_input == 'd':

                    def __init__(self,amount):
                        self.amount = amount

                    if user_input == 'w':

                        def withdrawal(self,withdrawal):
                            try:
                                totle = self.amount - withdrawal
                            except ValueError:
                                totle = 0
                            
                            with open('withdrawal_data.txt', 'w') as file:
                                file.write(f"Your Withdrawal Value is Rs {withdrawal}/= \nYour Totle Amount is Rs {totle}/= \n \t\t\t Thanks and Come agian...")

                    if user_input == 'd':

                        def deposit(self,deposit):
                            try:
                                totle = self.amount + deposit
                            except ValueError:
                                totle = 0

                            with open('deposit.txt', 'w') as file:
                                file.write(f"Your Deposit Value is Rs {deposit}/= \nYour Totle Amount is Rs {totle}/= \n \t\t\t Thanks and Come again...")

                    break
        break
    except ValueError:
        print('Please Enter Istring Value')



bank = Bank(totle_value)

if bank.user_input == 'w':
    withdrawal_value = int(input('Enter Your Withdrawal Value: '))
    bank.withdrow(withdrawal_value)

if bank.user_input == 'd':
    deposit_value = int(input('Enter Your Deposit Value: '))
    bank.deposit(deposit_value)

