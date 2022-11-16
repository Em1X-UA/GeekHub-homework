import sqlite3
from datetime import datetime
from settings import atm_data
from modules.system_modules import clear, determine_value


class Atm:
    @staticmethod
    def atm_balance():
        atm_cash = 0
        with sqlite3.connect(atm_data) as db:
            cursor = db.cursor()
            for nominal, q_ty in cursor.execute("SELECT * FROM banknotes_qty"):
                atm_cash += nominal * q_ty
        return atm_cash

    @staticmethod
    def available_banknotes():
        with sqlite3.connect(atm_data) as db:
            cursor = db.cursor()
            available = {}
            for nominal, q_ty in cursor.execute("SELECT * FROM banknotes_qty"):
                if q_ty > 0:
                    available.update({nominal: q_ty})
        return available

    @staticmethod
    def get_user_balance(user):
        with sqlite3.connect(atm_data) as db:
            cursor = db.cursor()
            balance = cursor.execute("SELECT balance FROM users_data "
                                     "WHERE user = ?", [user]).fetchone()[0]
        balance = determine_value(balance)
        return balance

    @staticmethod
    def change_user_balance(user, operation, amount):
        if operation == 'withdraw':
            amount = -amount
        with sqlite3.connect(atm_data) as db:
            cursor = db.cursor()
            cursor.execute("UPDATE users_data SET balance = balance + ? "
                           "WHERE user = ?", [amount, user])
        remaining = Atm.get_user_balance(user)
        Atm.logger(user, operation, amount, remaining)

    @staticmethod
    def logger(user, operation, amount, balance):
        if amount > 0 and ('top up' in operation.lower()):
            amount = f'+{amount}'
        data = (user, str(datetime.now()), operation, amount, balance)
        with sqlite3.connect(atm_data) as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO transaction_logs(""user, date, "
                           "operation, balance_changes, remaining"") "
                           "VALUES (?, ?, ?, ?, ?)", data)

    @staticmethod
    def get_banknotes():
        with sqlite3.connect(atm_data) as db:
            cursor = db.cursor()
            banknotes = {}
            for nominal, qty in cursor.execute("SELECT * FROM banknotes_qty"):
                banknotes[nominal] = qty
            return banknotes

    @staticmethod
    def get_all_logs():
        with sqlite3.connect(atm_data) as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM transaction_logs")
            full_log = cursor.fetchall()
            return full_log

    @staticmethod
    def get_user_log(user):
        with sqlite3.connect(atm_data) as db:
            cursor = db.cursor()
            user_transactions = []
            for id_op, user_log, date, operation, balance_changes, remaining \
                    in cursor.execute("SELECT * FROM transaction_logs"):
                if user == user_log:
                    user_transactions.append((id_op, date, operation,
                                              balance_changes, remaining))
            return user_transactions

    @staticmethod
    def get_banknote_qty(nominal_1):
        with sqlite3.connect(atm_data) as db:
            cursor = db.cursor()
            qty = cursor.execute("SELECT quantity FROM banknotes_qty "
                                 "WHERE nominal = ?", [nominal_1]).fetchone()[0]
            return qty

    @staticmethod
    def change_banknotes_qty(user, nominal_1, qty):
        with sqlite3.connect(atm_data) as db_1:
            cursor1 = db_1.cursor()
            cursor1.execute("UPDATE banknotes_qty SET quantity = ?"
                            "WHERE nominal = ?", [qty, nominal_1])
        Atm.logger(user, f'banknotes UAH {nominal_1} set', qty, Atm.atm_balance())
        print('ATM banknotes balance changed!')
        input('Press any key and (or just) ENTER to back main menu')
        clear()

    @staticmethod
    def count_cash(amount):
        """greedy algorithm"""
        available = Atm.available_banknotes()
        banknotes = sorted(available.keys(), reverse=True)
        banknotes_count = {}
        for banknote in banknotes:
            if amount >= banknote:
                x = amount // banknote
                if x <= available.get(banknote):
                    banknotes_count.update({banknote: x})
                    amount %= banknote
                else:
                    x = available.get(banknote)
                    banknotes_count.update({banknote: x})
                    amount -= banknote * x
        return banknotes_count

    @staticmethod
    def cash_reduce(banknotes: dict):
        with sqlite3.connect(atm_data) as db:
            cursor = db.cursor()
            for nominal_1, qty in banknotes.items():
                cursor.execute("UPDATE banknotes_qty SET quantity = quantity - ? "
                               "WHERE nominal = ?", [qty, nominal_1])
