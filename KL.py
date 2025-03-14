import random

def roll_dice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]

def player_turn(player_name):
    dice = roll_dice(5)
    kept_values = []
    
    while dice:
        min_value = min(dice)
        kept_values.append(min_value)
        dice.remove(min_value)
        if dice:
            dice = roll_dice(len(dice))
    
    turn_score = sum(kept_values)
    print(f"{player_name} kept {kept_values} for a total of {turn_score} points this turn.")
    return turn_score

def play_game():
    scores = {"Player 1": 0, "Player 2": 0}
    turn = 0
    
    while True:
        player = "Player 1" if turn % 2 == 0 else "Player 2"
        print(f"\n{player}'s turn:")
        scores[player] += player_turn(player)
        print(f"Scores: {scores}")
        
        if scores[player] >= 20:
            print(f"{player} reaches 20 points and loses the game! {player} loses!")
            break
        
        turn += 1

if __name__ == "__main__":
    play_game()
