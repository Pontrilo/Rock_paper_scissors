import random

options = ["rock", "paper", "scissors"]
outcome = ["draw", "lose", "win"]

playerScore = 0
pcScore = 0

leave = True

while leave:
    comp = random.randint(0, 2)
    pMove = input("Please enter your move, or enter exit: ")
    print("PC's move: {}".format(options[comp]))
    if pMove in options:
        moveIndex = options.index(pMove)
        result = (comp - moveIndex) % 3
        if result == 1:
            pcScore += 1
        elif result == 2:
            playerScore += 1
        print("You {} ... Your score: {},   PC score: {}".format(outcome[result].upper(), playerScore, pcScore))
    elif pMove == "exit":
        leave = False
    else:
        print("Please enter either rock, paper, scissors or exit")


