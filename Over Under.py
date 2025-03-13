player1score = 0
player2score = 0 
player1wins = 0
player2wins = 0

def diceroll():
    import random
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    return dice1 + dice2 + dice3

def player1():
    global player1score
    player1score = diceroll()

def player2():
    global player2score
    player2score = diceroll()

current_player = 1  
while True:
    player1()
    player2()
    
    if current_player == 1:
        print("Player 1 rolled: " + str(player1score))
        input_choice = input("Player 2, enter over or under: ")
    else:
        print("Player 2 rolled: " + str(player2score))
        input_choice = input("Player 1, enter over or under: ")
    
    if input_choice == "over":
        if current_player == 1:
            if player1score > player2score:
                print("Player 1 wins")
                player1wins += 1 
                current_player = 1  
                print("Player 1 score: " + str(player1score))
            else:
                print("Player 2 wins")
                player2wins += 1  
                current_player = 2  
                print("Player 2 score: " + str(player2score))
        else:
            if player2score > player1score:
                print("Player 2 wins")
                player2wins += 1 
                current_player = 2  
                print("Player 2 score: " + str(player2score))
            else:
                print("Player 1 wins")
                player1wins += 1  
                current_player = 1  
                print("Player 1 score: " + str(player1score))
    else:  
        if current_player == 1:
            if player1score < player2score:
                print("Player 1 wins")
                player1wins += 1 
                current_player = 1  
                print("Player 1 score: " + str(player1score))
            else:
                print("Player 2 wins")
                player2wins += 1  
                current_player = 2  
                print("Player 2 score: " + str(player2score))
        else:
            if player2score < player1score:
                print("Player 2 wins")
                player2wins += 1 
                current_player = 2  
                print("Player 2 score: " + str(player2score))
            else:
                print("Player 1 wins")
                player1wins += 1  
                current_player = 1  
                print("Player 1 score: " + str(player1score))

    print("Player 1 wins: " + str(player1wins))
    print("Player 2 wins: " + str(player2wins))

    play_again = input("Do you want to play another round? (yes/no): ")
    if play_again.lower() != "yes":
        break
