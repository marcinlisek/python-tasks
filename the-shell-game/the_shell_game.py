import random


def players_guess():
    guess = ""

    while guess not in ["l", "c", "r"]:
        guess = input("Enter the position: l for left, c for center, r for right: \n")

    if guess == "l":
        return 0
    elif guess == "c":
        return 1
    elif guess == "r":
        return 2


def check_guess(game_list, guess):
    if game_list[guess] == "o":
        return True

    else:
        return False


gameon = True

counter_p1 = 0
counter_p2 = 0

win_check_p1 = "N"
win_check_p2 = "N"

Turn = "Player_1"

game_list = [" ", "o", " "]


while gameon:

    if Turn == "Player_1" and win_check_p1 == "N":
        print("Turn Player 1")

        random.shuffle(game_list)

        guess = players_guess()

        if check_guess(game_list, guess):
            counter_p1 += 1
            win_check_p1 = "Y"
            Turn = "Player_2"
            print("You guessed correctly!")
            print(game_list)
            print("")
            if win_check_p2 == "Y":
                Turn = "Player_1"

        else:
            counter_p1 += 1
            Turn = "Player_2"
            print("You guessed wrong!")
            print(game_list)
            print("")
            if win_check_p2 == "Y":
                Turn = "Player_1"

    elif Turn == "Player_2" and win_check_p2 == "N":
        print("Turn Player 2")

        random.shuffle(game_list)

        guess = players_guess()

        if check_guess(game_list, guess):
            counter_p2 += 1
            win_check_p2 = "Y"
            Turn = "Player_1"
            print("You guessed correctly!")
            print(game_list)
            print("")
            if win_check_p1 == "Y":
                Turn = "Player_2"

        else:
            counter_p2 += 1
            Turn = "Player_1"
            print("You guessed wrong!")
            print(game_list)
            print("")
            if win_check_p1 == "Y":
                Turn = "Player_2"

    elif win_check_p1 == "Y" and win_check_p2 == "Y":
        gameon = False
        if counter_p1 < counter_p2:
            print(f"Player 1 guessed correctly in {counter_p1} turns, and Player 2 guessed correctly in {counter_p2} turns.\nPlayer 1 WINS!")

        else:
            print(f"Player 1 guessed correctly in {counter_p1} turns, and Player 2 guessed correctly in {counter_p2} turns.\nPlayer 2 WINS!")
