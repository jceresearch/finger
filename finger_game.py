# main loop for finger game to check how deep is the tree/game and who wins
# %%
import pandas as pd
import numpy as np
import random


class Hands:
    def __init__(self, left_hand, right_hand, player_name):
        self.left_hand = 1
        self.right_hand = 1
        self.player_name = player_name

    def __str__(self):
        if self.left_hand <= 0:
            left_hand_str = "Out"
        else:
            left_hand_str = str(self.left_hand)
        if self.right_hand <= 0:
            right_hand_str = "Out"
        else:
            right_hand_str = str(self.right_hand)
        return f"Player {self.player_name}: Left hand: {left_hand_str}, Right hand: {right_hand_str}"

    # method to check if the game is over
    def is_game_lost(self):
        return self.left_hand <= 0 and self.right_hand <= 0

    # method to react to a touch
    def touch_hand(self, hand, number_of_fingers):
        if hand == 1 and number_of_fingers > 0:
            self.left_hand += number_of_fingers
            if self.left_hand>5 and self.right_hand>0:
                self.right_hand += self.left_hand-5
        elif hand == 2 and number_of_fingers > 0:
            self.right_hand += number_of_fingers
            if self.right_hand>5 and self.left_hand>0:
                self.left_hand += self.right_hand-5
        else:
            raise ValueError("Invalid hand or number of fingers")
        if self.left_hand >= 5:
            self.left_hand = 0
        if self.right_hand >= 5:
            self.right_hand = 0
            
    def hands_available(self):
        available_hands=[]
        if self.left_hand>0:
            available_hands.append(1)
        if self.right_hand>0:
            available_hands.append(2)
        return available_hands


# %%
# main loop to play the game

def play_game(trace=False):
    player1 = Hands(1, 1, "Lu")
    player2 = Hands(1, 1, "Dad")
    turn_count = 0
    game_trace=[]
    while not (player1.is_game_lost() or player2.is_game_lost()):
        turn_count += 1
        # Player 1's turn
        hand_to_touch = random.choice(player2.hands_available())
        number_of_fingers = random.randint(1, 4)
        player2.touch_hand(hand_to_touch, number_of_fingers)
        game_trace.append(hand_to_touch*10+number_of_fingers) 
        if trace:
            print(f"{player1} touched hand {hand_to_touch} with {number_of_fingers} fingers")
        if player2.is_game_lost():
            break
        # Player 2's turn
        hand_to_touch = random.choice(player1.hands_available())
        number_of_fingers = random.randint(1, 4)
    
        player1.touch_hand(hand_to_touch, number_of_fingers)
        if trace:
            print(f"{player2} touched hand {hand_to_touch} with {number_of_fingers} fingers ")
        game_trace.append(hand_to_touch*10+number_of_fingers)
        if player1.is_game_lost():
            break
        if trace: 
            print(f"At end of turn:")
            print(f"{player1}")
            print(f"{player2}")
    if player1.is_game_lost():
        if trace:
            print("Won 1 in turns:", turn_count, "Trace:",game_trace)
        return (1,turn_count,game_trace)
    elif player2.is_game_lost():
        if trace:
            print("Won 2 in turns:", turn_count, "Trace:",game_trace)
        return(2,turn_count,game_trace)

game_results=[]
game_length=[]
number_games=1000000
for n in range(0 ,number_games):
    res=play_game()
    game_results.append(res[0])
    game_length.append(res[1])
    
from collections import Counter


counts = Counter(game_results)
print("Number of games", len(game_results))
print("Player 1", counts[1]) 
print("Player 2", counts[2])  
counts2 = Counter(game_length)

import numpy as np
from pprint import pprint
unique, counts = np.unique(game_length, return_counts=True)
count_dict = dict(zip(unique, counts))
pprint(count_dict)

