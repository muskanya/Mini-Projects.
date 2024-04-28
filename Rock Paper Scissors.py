# Rock Paper Scissors

print("Welcome to Rock Paper Scissors game")
mode = int(input("Enter which mode do you want to play: 2 players mode or 3 players mode: "))

while True:
    if mode == 2:
        print("You have selected 2 players mode")
        p1 = input("Player 1, Please enter your name: ")
        p2 = input("Player 2, Please enter your name: ")

        while True:
            c1 = input(f"{p1}, choose between: ROCK, PAPER, SCISSOR: ").upper()
            if c1 not in ["ROCK", "PAPER", "SCISSOR"]:
                print("INVALID INPUT")
                continue
            else:
                break

        while True:
            c2 = input(f"{p2}, choose between: ROCK, PAPER, SCISSOR: ").upper()
            if c2 not in ["ROCK", "PAPER", "SCISSOR"]:
                print("INVALID INPUT")
                continue
            else:
                break

        if c1 == c2:
            print("It's a Tie. TRY AGAIN")
        elif (c1 == "ROCK" and c2 == "SCISSOR") or (c1 == "PAPER" and c2 == "ROCK") or (c1 == "SCISSOR" and c2 == "PAPER"):
            print(f"{p1} WON")
        else:
            print(f"{p2} WON")

    elif mode == 3:
        print("You have selected 3 players mode")
        p1 = input("Player 1, Please enter your name: ")
        p2 = input("Player 2, Please enter your name: ")
        p3 = input("Player 3, Please enter your name: ")

        while True:
            c1 = input(f"{p1}, choose between: ROCK, PAPER, SCISSOR: ").upper()
            if c1 not in ["ROCK", "PAPER", "SCISSOR"]:
                print("INVALID INPUT")
                continue
            else:
                break

        while True:
            c2 = input(f"{p2}, choose between: ROCK, PAPER, SCISSOR: ").upper()
            if c2 not in ["ROCK", "PAPER", "SCISSOR"]:
                print("INVALID INPUT")
                continue
            else:
                break

        while True:
            c3 = input(f"{p3}, choose between: ROCK, PAPER, SCISSOR: ").upper()
            if c3 not in ["ROCK", "PAPER", "SCISSOR"]:
                print("INVALID INPUT")
                continue
            else:
                break

        if c1 == c2 == c3:
            print("It's a Tie. TRY AGAIN")
        elif (c1 == "ROCK" and c2 == "SCISSOR" and c3 == "SCISSOR") or (c1 == "PAPER" and c2 == "ROCK" and c3 == "ROCK") or (c1 == "SCISSOR" and c2 == "PAPER" and c3 == "PAPER"):
            print("It's a Tie. TRY AGAIN")
        elif (c1 == "ROCK" and c2 == "SCISSOR" and c3 == "PAPER") or (c1 == "PAPER" and c2 == "ROCK" and c3 == "SCISSOR") or (c1 == "SCISSOR" and c2 == "PAPER" and c3 == "ROCK"):
            print(f"{p1} WON")
        elif (c1 == "ROCK" and c2 == "PAPER" and c3 == "SCISSOR") or (c1 == "PAPER" and c2 == "SCISSOR" and c3 == "ROCK") or (c1 == "SCISSOR" and c2 == "ROCK" and c3 == "PAPER"):
            print(f"{p2} WON")
        else:
            print(f"{p3} WON")

    else:
        print("INVALID CHOICE, Choose again")
        mode = int(input("Enter which mode do you want to play: 2 players mode or 3 players mode: "))

    ask = input("Want to play again? 'y' for yes and 'n' for no: ").lower()
    if ask == "y":
        continue
    elif ask == "n":
        break
    else:
        print("Invalid choice. Exiting game.")
        break