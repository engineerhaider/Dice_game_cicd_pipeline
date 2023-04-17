import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the dice game!")
    print("You will roll the dice twice. If your second roll is higher than your first, you win.")

    input("Press enter to roll the dice for the first time...")
    roll1 = roll_dice()
    print("You rolled a", roll1)

    input("Press enter to roll the dice for the second time...")
    roll2 = roll_dice()
    print("You rolled a", roll2)

    if roll2 > roll1:
        print("Congratulations, you win!")
    elif roll2 == roll1:
        print("It's a tie!")
    else:
        print("Sorry, you lose.")

if __name__ == '__main__':
    main()
