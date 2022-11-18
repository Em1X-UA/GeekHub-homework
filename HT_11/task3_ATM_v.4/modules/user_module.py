from settings import input_attempts, banknotes_list
from modules.system_modules \
    import slp, clear, get_user_choice, get_user_input
from modules.atm_module import Atm


class User:
    def __init__(self, name):
        self.name = name

    def user_menu(self):
        """Main menu"""

        from main import start

        clear()
        print('What do you want to do?')
        print('1. Check balance')
        print('2. Withdraw money')
        print('3. Top up the balance')
        print('4. Transactions history\n')
        print('0. Exit\n')

        user_choice = get_user_choice(4)
        match user_choice:
            case 1:
                return self.check_balance()
            case 2:
                return self.withdraw_money()
            case 3:
                return self.top_up_balance()
            case 4:
                return self.check_logs()
            case '0':
                print(f'Goodbye {self.name}!')
                slp()
                clear()
                start()

    def check_balance(self):
        user = self.name
        balance = Atm.get_user_balance(user)
        print(f'You have {balance} UAH\n')
        input('Press any key and (or just) ENTER to back main menu')
        return self.user_menu()

    def withdraw_money(self):
        clear()
        user = self.name
        min_banknote = min(Atm.available_banknotes())

        attempts = input_attempts
        for _ in range(input_attempts):
            print('Enter the amount, you want to withdraw!')
            if attempts < input_attempts:
                print('Or input "0" top back main menu!')

            print(f'The amount must be a multiple of {min_banknote}!')
            user_input = get_user_input()
            if attempts < input_attempts:
                if user_input == 0:
                    clear()
                    return self.user_menu()

            try:
                if user_input > Atm.get_user_balance(user):
                    print('You don\'t gave enough money!')
                    raise ValueError
                elif user_input % min_banknote != 0:
                    print('Impossible to withdraw funds with existing banknotes: ')
                    raise ValueError
                elif user_input > Atm.atm_balance():
                    print('Sum is too much! \nATM doesn\'t have enough money!')
                    raise ValueError
                elif user_input <= 0:
                    print('You can\'t withdraw negative (or zero) amount!')
                    raise ValueError
                else:
                    banknotes = Atm.count_cash(user_input)
                    print(banknotes)
                    check_sum = sum([nominal * qty for nominal, qty in banknotes.items()])
                    if check_sum != user_input:
                        print('Looks like not enough banknotes in ATM. \n'
                              'You can try another amount')
                        slp()
                        continue

                    Atm.cash_reduce(banknotes)
                    Atm.change_user_balance(user, 'withdraw', user_input)

                    clear()
                    print('==================')
                    for nominal, qty in banknotes.items():
                        print(f'{nominal} UAH x {qty} pc')
                    print('==================')

                    print(f'{user_input} UAH successfully withdrawn')
                    input('Press any key and (or just) ENTER to back main menu')
                    clear()
                    return self.user_menu()

            except ValueError:
                attempts -= 1
                print(f'Incorrect amount entered. {attempts} attempts left.')
                slp()
                clear()
                continue
        print('All attempts failed. Returning main menu.')
        slp()
        clear()
        return self.user_menu()

    def top_up_balance(self):
        user = self.name
        min_banknote = min(banknotes_list)
        clear()
        attempts = input_attempts
        for _ in range(input_attempts):
            print('Enter the amount by which you want to top up your account.')
            if attempts < input_attempts:
                print('Or input "0" top back main menu!')
            print(f'The minimum banknote for top-up is {min_banknote}!')
            user_input = get_user_input()
            if attempts < input_attempts:
                if user_input == 0:
                    clear()
                    self.user_menu()

            try:
                if user_input == 0:
                    print('You can\'t add zero amount to your balance!')
                    raise ValueError
            except ValueError:
                attempts -= 1
                print(f'Incorrect amount entered. Try again! {attempts} attempts left.')
                slp()
                clear()
                continue
            else:
                if user_input % min_banknote != 0:
                    print(f'ATM accepts banknotes with a minimum denomination '
                          f'of {min_banknote}')
                    print(f'Take your {user_input % min_banknote} UAH back!')
                    user_input -= user_input % min_banknote
                Atm.change_user_balance(user, 'Top up', user_input)

                print(f'Your account has been topped up by {user_input} UAH.')
                input('Press any key and (or just) ENTER to back main menu')
                clear()
                return self.user_menu()

        print('All attempts failed. Returning main menu.')
        slp()
        clear()
        return self.user_menu()

    def check_logs(self):
        log = Atm.get_user_log(self.name)
        for id_op, date, operation, balance_changes, remaining in log:
            print(f'ID: {id_op}')
            print(f'Date: {date}')
            print(f'Operation: {operation}')
            print(f'Balance change: {balance_changes}')
            print(f'Remaining balance: {remaining}')
            print('=======================')
        input('\nPress any key and (or just) ENTER to back main menu')
        clear()
        return self.user_menu()
