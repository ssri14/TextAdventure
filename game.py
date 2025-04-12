import random

def play_game():
    print("\nWelcome to the Text Adventure Game!")
    print("You're standing at the edge of a dark forest.")
    print("You have two choices: go left or go right.")
    choice = input("Which way do you go? (left/right): ")
    if choice.lower() == "left":
        outcomes = [
            "You meet a wise old man who shares forest secrets.",
            "A friendly elf shows you a hidden treasure path."
        ]
    elif choice.lower() == "right":
        outcomes = [
            "A wild boar chases you, but you escape!",
            "You discover a magical cave with glowing crystals."
        ]
    else:
        outcomes = ["You wander aimlessly and eventually get lost."]
    print(random.choice(outcomes))
if __name__ == "__main__":
    while True:
        play_game()
        replay = input("\nDo you want to play again? (yes/no): ")
        if replay.lower() != "yes":
            print("Thanks for playing!")
            break
