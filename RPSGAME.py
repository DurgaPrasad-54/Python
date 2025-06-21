import random 
choices = ['rock','paper',"scissor"]

while True:
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock,paper,scissor?:").lower()
        print("computer:",computer)
        print("player:",player)
        if(computer == player):
            print("TIE!")
        elif(player=="rock"):
            if(computer=="paper"):
                print('YOU LOSE')
            if(computer == "scissor"):
                print("YOU WON")
        elif(player=="paper"):
            if(computer=="scissor"):
                print("YOU LOSE")
            if(computer == "rock"):
                print("YOU WON")
        elif(player == "scissor"):
            if(computer == "paper"):
                print ("YOU LOSE")
            if(computer == "rock"):
                print("YOU WIN")
    play = input("PLAY AGAIN YES/NO: ").lower()
    if(play != 'yes'):
        break
print(" bye")
            