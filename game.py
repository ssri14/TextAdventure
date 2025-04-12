# game.py (v1.0)
def play_game():
    print("\nWelcome to the Text Adventure Game!")
    print("You're standing at the edge of a dark forest.")
    print("You have two choices: go left or go right.")
    choice = input("Which way do you go? (left/right): ")

    if choice.lower() == "left":
        print("You meet a friendly wizard who offers you a magic potion!")
    elif choice.lower() == "right":
        print("You encounter a wild wolf and manage to escape!")
    else:
        print("Unable to decide, you remain until nightfall. The game ends.")

if __name__ == "__main__":
    while True:
        play_game()
        replay = input("\nDo you want to play again? (yes/no): ")
        if replay.lower() != "yes":
            print("Thanks for playing!")
            break
