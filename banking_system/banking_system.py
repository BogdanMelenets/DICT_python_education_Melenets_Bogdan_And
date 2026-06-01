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