# Lab 25: ATM, version 3

class ATM:
    def __init__(self, balance=0, interest=0.1):
        self.balance = balance
        self.interest = interest

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def check_withdrawal(self, amount):
        if self.balance >= amount:
            return True
        return False

    def withdraw(self, amount):
        if self.check_withdrawal(amount) == True:
            self.balance -= amount
            return self.balance
        return 'Insufficient funds. Transaction could not be completed.'

    def calc_interest(self):
        return f'Your interest: {self.balance * self.interest}'

    def print_transactions(self, trans_list):
        for transaction in trans_list:
            print(transaction)


if __name__ == '__main__':
    new_account = ATM()
    trans_history = []
    while True:
        account_activity = input('Would you like to make a (d)eposit, make a (w)ithdrawal, (c)heck balance, or view transaction (h)istory?\nOtherwise, e(x)it.\n').strip().lower()

        if account_activity in ['x', 'exit', 'q', 'quit']:
            break

        if account_activity.startswith('d'):
            deposit_amt = int(input('How much would you like to deposit? ').strip())
            new_account.deposit(deposit_amt)
            trans_history.append(f'User deposited {deposit_amt}.')
        if account_activity.startswith('w'):
            withdrawal_amt = int(input('How much would you like to withdraw? ').strip())
            withdrawn = new_account.withdraw(withdrawal_amt)
            if withdrawn == 'Insufficient funds. Transaction could not be completed.':
                print(withdrawn)
            else:
                trans_history.append(f'User withdrew {withdrawal_amt}.')
        if account_activity.startswith('c'):
            print(f'Your current balance: ${new_account.check_balance()}')
        if account_activity.startswith('h'):
            new_account.print_transactions(trans_history)
