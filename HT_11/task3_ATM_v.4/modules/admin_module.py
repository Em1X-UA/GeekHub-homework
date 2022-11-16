from settings import banknotes_list
from modules.system_modules import clear, slp, get_user_choice, get_user_input
from modules.atm_module import Atm


class Admin:
    def __init__(self, name):
        self.name = name

    def user_menu(self):
        from main import start
        print('What do you want to do?')
        print('1. Check ATM balance')
        print('2. Check banknotes balance')
        print('3. Change banknotes balance')
        print('4. Your transactions history')
        print('5. All transactions history\n')
        print('0. Exit\n')

        user_choice = get_user_choice(5)
        match user_choice:
            case 1:
                return self.check_atm_balance()
            case 2:
                return self.check_banknotes()
            case 3:
                return self.change_banknotes_balance_menu()
            case 4:
                return self.check_logs()
            case 5:
                return self.check_all_logs()
            case 0:
                print(f'Goodbye {self.name}!')
                slp()
                clear()
                start()

    def check_atm_balance(self):
        print(f'ATM has {Atm.atm_balance()} UAH\n')
        input('Press any key and (or just) ENTER to back main menu')
        clear()
        return self.user_menu()

    def check_banknotes(self):
        print('Nominal | Quantity')
        for nominal, qty in Atm.get_banknotes().items():
            print(f'{nominal} UAH: {qty} pcs')
        input('\nPress any key and (or just) ENTER to back main menu')
        clear()
        return self.user_menu()

    def change_banknotes_balance_menu(self):
        clear()
        print('Choose banknote nominal to change quantity')
        counter = 1
        for banknote in banknotes_list:
            print(f'{counter}. UAH {banknote}')
            counter += 1
        print('\n0. Back to main menu\n')
        user_choice = get_user_choice(len(banknotes_list))
        clear()
        if user_choice == 0:
            return self.user_menu()
        user_choice -= 1
        chosen_nominal = banknotes_list[user_choice]
        print(f'Current quantity of {chosen_nominal} UAH '
              f'is {Atm.get_banknote_qty(chosen_nominal)}\n')
        user_input = get_user_input()
        Atm.change_banknotes_qty(self.name, chosen_nominal, user_input)
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

    # check working....
    def check_all_logs(self):
        clear()
        print(f'---All users transactions history---')
        for id_op, user_log, date, operation, balance_changes, remaining in \
                Atm.get_all_logs():
            print(f'ID: {id_op}')
            print(f'User: {user_log}')
            print(f'Date: {date}')
            print(f'Operation: {operation}')
            print(f'Balance change: {balance_changes}')
            print(f'Remaining balance: {remaining}')
            print('=======================')
        input('Press any key and (or just) ENTER to back main menu')
        clear()
        return self.user_menu()
