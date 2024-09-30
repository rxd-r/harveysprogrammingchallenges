from random import choices


def run_fruit_machine():
    symbols = ["🍒", "🔔", "🍋", "🍊", "⭐", "💀"]

    credit: int = 100
    while credit > 0:
        print(f"Current Balance: {credit}p")
        if input("Quit? [Y/n]") == "Y":
            break

        rolls = choices(symbols, k=3)
        print(f"You rolled {rolls[0]}{rolls[1]}{rolls[2]}")

        if rolls[0] == rolls[1] and rolls[1] == rolls[2]:
            if rolls[0] == "💀":
                credit = 0
            else:
                credit += 100
        elif rolls[0] == rolls[1] or rolls[1] == rolls[2] or rolls[0] == rolls[2]:
            index = 1
            if rolls[0] == rolls[2]:
                index = 0

            if rolls[index] == "💀":
                credit -= 100
            else:
                credit += 50

    print(f"You finished with {credit}p")
