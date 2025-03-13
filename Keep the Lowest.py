import random

player1score = 0
player2score = 0

def diceroll():
    dice = [random.randint(1, 6) for _ in range(5)]
    kept_dice = []

    while dice:
        lowest = min(dice)
        kept_dice.append(lowest)
        dice.remove(lowest)
        dice = [random.randint(1, 6) for _ in range(len(dice))]

    return sum(kept_dice)

def play_turn(player):
    global player1score, player2score
    score = diceroll()
    if player == 1:
        player1score += score
        print(f"Player 1 rolled and kept dice summing to {score}. Total score: {player1score}")
    else:
        player2score += score
        print(f"Player 2 rolled and kept dice summing to {score}. Total score: {player2score}")

def main():
    current_player = 1
    while player1score < 20 and player2score < 20:
        play_turn(current_player)
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1

    if player1score >= 20:
        print("Player 1 loses")
    elif player2score >= 20:
        print("Player 2 loses")

if __name__ == "__main__":
    main()