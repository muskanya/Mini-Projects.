# Roll the dice

import random
while True:
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    # 56 steps
    p1=input("Player 1 ! Please enter your name: ")
    p2 = input("Player 2 ! Please enter your name: ")
    p3 = input("Player 3 ! Please enter your name: ")
    while True:
        choose=input("Do you want computer as 4th player or not, (choose C for computer and P for real player: ").upper()

        if choose == "P":
            p4 = input("Player 4 ! Please enter your name: ")
        elif choose=="C":
            print("Now! Computer is playing with you all as Player 4")
        else:
            print("!INVALID CHOICE! Choose Again")
            continue
        break
    while True:
        while True:
            n1 = int(input(f"{p1} ,\"Enter a number between 1 and 6:\" "))
            if n1 < 1 or n1 > 6:
                print(f"!Error! {p1} ,\"Please enter a number between 1 and 6 not lower than 1 and not greater than 6\"")
                continue
            else:
                s1+=n1
                break
        while True:
            n2 = int(input(f"{p2} ,\"Enter a number between 1 and 6:\" "))
            if n2 < 1 or n2 > 6:
                print(f"!Error! {p2},\"Please enter a number between 1 and 6 not lower than 1 and not greater than 6\"")
                continue
            else:
                s2 += n2
                break
        while True:
            n3 = int(input(f"{p3} ,\"Enter a number between 1 and 6:\" "))
            if n3 < 1 or n3 > 6:
                print(f"!Error! {p3},\"Please enter a number between 1 and 6 not lower than 1 and not greater than 6\"")
                continue
            else:
                s3+=n3
                break
        while True:
            if choose=="P":
                n4 = int(input(f"{p4} ,\"Enter a number between 1 and 6:\" "))
                if n4 < 1 or n4 > 6:
                    print("!Error!Please enter a number between 1 and 6 not lower than 1 and not greater than 6")
                    continue
                else:
                    s4 += n4
                    break
            else:
                c=random.randint(0,6)
                s4 += c
                break
        if s1>=56 and s2!=56 and s3!=56 and s4!=56:
            print(f"{p1}, WON the game")
            break
        elif s1!=56 and s2>=56 and s3!=56 and s4!=56:
            print(f"{p2}, WON the game")
            break
        elif s1!=56 and s2==56 and s3>=56 and s4!=56:
            print(f"{p3}, WON the game")
            break
        elif s1!=56 and s2!=56 and s3!=56 and s4>=56:
            if choose=="P":
                print(f"{p4}, WON the game")
                break
            else:
                print("Computer , WON the game")
                break
        else:
            print("!NOW!, Another round is in play")
            continue
    break