import random
from curses.ascii import isdigit
from webbrowser import get

NUM_MAX_LINES = 3
MAX_BET = 100 #dollars
MIN_BET = 1 #dollars
NUM_ROWS = 3
NUM_COLS = 3

symbol_count = { #define the number of symbols
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit(): # check that amount is a digit
            amount = int(amount) # type amount to int
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(NUM_MAX_LINES) + ")?")
        if lines.isdigit(): # check that amount is a digit
            lines = int(lines) # type amount to int
            if 1 <= lines <= NUM_MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit(): # check that amount is a digit
            amount = int(amount) # type amount to int
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("please enter a number.")
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

main()

