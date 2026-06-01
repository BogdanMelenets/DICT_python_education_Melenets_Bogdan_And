import random

accounts = {}


def generate_card_number():
    while True:
        account_number = str(random.randint(0, 999999999)).zfill(9)
        check_digit = str(random.randint(0, 9))
        card_number = "400000" + account_number + check_digit

        if card_number not in accounts:
            return card_number


def generate_pin():
    return str(random.randint(0, 9999)).zfill(4)


while True:
    print("\n1. Create an account")
    print("2. Log into account")
    print("0. Exit")

    choice = input()

    if choice == "1":
        card_number = generate_card_number()
        pin = generate_pin()

        accounts[card_number] = {
            "pin": pin,
            "balance": 0
        }

        print("\nYour card has been created")
        print("Your card number:")
        print(card_number)
        print("Your card PIN:")
        print(pin)

    elif choice == "2":
        print("\nEnter your card number:")
        card_number = input()

        print("Enter your PIN:")
        pin = input()

        if (card_number in accounts and
                accounts[card_number]["pin"] == pin):

            print("\nYou have successfully logged in!")

            while True:
                print("\n1. Balance")
                print("2. Log out")
                print("0. Exit")

                account_choice = input()

                if account_choice == "1":
                    print(f"\nBalance: {accounts[card_number]['balance']}")

                elif account_choice == "2":
                    print("\nYou have successfully logged out!")
                    break

                elif account_choice == "0":
                    print("\nBye!")
                    exit()

        else:
            print("\nWrong card number or PIN!")

    elif choice == "0":
        print("\nBye!")
        break

import random

accounts = {}


def generate_pin():
    return str(random.randint(0, 9999)).zfill(4)


def luhn_checksum(number):
    digits = [int(x) for x in number]

    for i in range(len(digits)):
        if i % 2 == 0:
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9

    total = sum(digits)
    return (10 - total % 10) % 10


def generate_card_number():
    while True:
        account_identifier = str(random.randint(0, 999999999)).zfill(9)

        card_without_checksum = "400000" + account_identifier

        checksum = luhn_checksum(card_without_checksum)

        card_number = card_without_checksum + str(checksum)

        if card_number not in accounts:
            return card_number


while True:
    print("1. Create an account")
    print("2. Log into the account")
    print("0. Exit")

    choice = input()

    if choice == "1":
        card_number = generate_card_number()
        pin = generate_pin()

        accounts[card_number] = {
            "pin": pin,
            "balance": 0
        }

        print("\nYour card has been created")
        print("Your card number:")
        print(card_number)
        print("Your card PIN:")
        print(pin)
        print()

    elif choice == "2":
        print("\nEnter your card number:")
        card = input()

        print("Enter your PIN:")
        pin = input()

        if card in accounts and accounts[card]["pin"] == pin:
            print("\nYou have successfully logged in!\n")

            while True:
                print("1. Balance")
                print("2. Log out")
                print("0. Exit")

                account_choice = input()

                if account_choice == "1":
                    print(f"\nBalance: {accounts[card]['balance']}\n")

                elif account_choice == "2":
                    print("\nYou have successfully logged out!\n")
                    break

                elif account_choice == "0":
                    print("\nBye!")
                    exit()

        else:
            print("\nWrong card number or PIN!\n")

    elif choice == "0":
        print("\nBye!")
        break

import sqlite3
import random


conn = sqlite3.connect("card.s3db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS card (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT,
    pin TEXT,
    balance INTEGER DEFAULT 0
);
""")

conn.commit()


def generate_pin():
    return str(random.randint(0, 9999)).zfill(4)


def luhn_checksum(number):
    digits = [int(d) for d in number]

    for i in range(len(digits)):
        if i % 2 == 0:
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9

    total = sum(digits)
    return str((10 - total % 10) % 10)


def generate_card_number():
    while True:
        account_identifier = str(
            random.randint(0, 999999999)
        ).zfill(9)

        card_without_checksum = "400000" + account_identifier

        card_number = (
            card_without_checksum +
            luhn_checksum(card_without_checksum)
        )

        cur.execute(
            "SELECT number FROM card WHERE number = ?",
            (card_number,)
        )

        if cur.fetchone() is None:
            return card_number


while True:
    print("1. Create an account")
    print("2. Log into the account")
    print("0. Exit")

    choice = input()

    if choice == "1":

        card_number = generate_card_number()
        pin = generate_pin()

        cur.execute("""
        INSERT INTO card(number, pin)
        VALUES(?, ?)
        """, (card_number, pin))

        conn.commit()

        print("\nYour card has been created")
        print("Your card number:")
        print(card_number)
        print("Your card PIN:")
        print(pin)
        print()

    elif choice == "2":

        print("\nEnter your card number:")
        card_number = input()

        print("Enter your PIN:")
        pin = input()

        cur.execute("""
        SELECT * FROM card
        WHERE number = ? AND pin = ?
        """, (card_number, pin))

        account = cur.fetchone()

        if account:
            print("\nYou have successfully logged in!\n")

            while True:
                print("1. Balance")
                print("2. Log out")
                print("0. Exit")

                account_choice = input()

                if account_choice == "1":

                    cur.execute("""
                    SELECT balance
                    FROM card
                    WHERE number = ?
                    """, (card_number,))

                    balance = cur.fetchone()[0]

                    print(f"\nBalance: {balance}\n")

                elif account_choice == "2":
                    print("\nYou have successfully logged out!\n")
                    break

                elif account_choice == "0":
                    print("\nBye!")
                    conn.close()
                    exit()

        else:
            print("\nWrong card number or PIN!\n")

    elif choice == "0":
        print("\nBye!")
        conn.close()
        break

def check_luhn(card_number):
    checksum = int(card_number[-1])
    number = card_number[:-1]

    digits = [int(d) for d in number]

    for i in range(len(digits)):
        if i % 2 == 0:
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9

    total = sum(digits) + checksum

    return total % 10 == 0

while True:

    print("1. Balance")
    print("2. Add income")
    print("3. Do transfer")
    print("4. Close account")
    print("5. Log out")
    print("0. Exit")

    account_choice = input()

    if account_choice == "1":

        cur.execute(
            "SELECT balance FROM card WHERE number = ?",
            (card_number,)
        )

        balance = cur.fetchone()[0]

        print(f"\nBalance: {balance}\n")

    elif account_choice == "2":

        print("\nEnter income:")
        income = int(input())

        cur.execute("""
        UPDATE card
        SET balance = balance + ?
        WHERE number = ?
        """, (income, card_number))

        conn.commit()

        print("Income was added!\n")

    elif account_choice == "3":

        print("\nTransfer")
        print("Enter card number:")

        destination = input()

        if destination == card_number:
            print("\nYou can't transfer money to the same account!\n")
            continue

        if not check_luhn(destination):
            print(
                "\nProbably you made a mistake "
                "in the card number. Please try again!\n"
            )
            continue

        cur.execute(
            "SELECT * FROM card WHERE number = ?",
            (destination,)
        )

        receiver = cur.fetchone()

        if receiver is None:
            print("\nSuch a card does not exist.\n")
            continue

        print("Enter how much money you want to transfer:")
        amount = int(input())

        cur.execute(
            "SELECT balance FROM card WHERE number = ?",
            (card_number,)
        )

        balance = cur.fetchone()[0]

        if amount > balance:
            print("\nNot enough money!\n")
            continue

        cur.execute("""
        UPDATE card
        SET balance = balance - ?
        WHERE number = ?
        """, (amount, card_number))

        cur.execute("""
        UPDATE card
        SET balance = balance + ?
        WHERE number = ?
        """, (amount, destination))

        conn.commit()

        print("\nSuccess!\n")

    elif account_choice == "4":

        cur.execute(
            "DELETE FROM card WHERE number = ?",
            (card_number,)
        )

        conn.commit()

        print("\nThe account has been closed!\n")
        break

    elif account_choice == "5":

        print("\nYou have successfully logged out!\n")
        break

    elif account_choice == "0":

        print("\nBye!")
        conn.close()
        exit()