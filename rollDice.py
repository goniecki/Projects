import random

def roll_dice():
    print("Rolling the dices")
    print("The values are: ")
    print(random.randint(1,6))
    print(random.randint(1, 6))
def main():
    print("This program rolls the dice")
    while True:
        try:
            decision = float(input("Do you want to roll the dice? 1 - yes / 2 - no, exit program: "))
        except ValueError:
            print("Wrong Value")
            break
        if decision == 1:
            roll_dice()
        if decision == 2:
            break
if __name__ == "__main__":
    main()
