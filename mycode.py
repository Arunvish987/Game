count = 0

import random
i = 0
while i<3:
    i=i+1
    player = input("rock , papper , sissor ?")
    computer = random.choice(["rock","papper","scissor"])

    if player == computer:
        print("tie!!!")

    elif player == "rock":
        if computer =="papper":
            print("you lose!1",computer,"covers",player)
        else:
            print("you win!",player,"smashes",computer)
    elif player == "papper":
        if computer == "scissor":
            print("you lose",computer,"cut",player)
        else:
            print("you win!!",player,"cover",computer)
    elif player == "scissor":
        if computer == "rock":
            print("you loose...",computer,"smaches",player)
        else:
            print("you win",player,"cut",computer)
    else:
        print("check you spelling")

print("come again....")