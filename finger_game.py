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
        if self.left_hand == -1:
            left_hand_str = "Left hand is out"
        else:
            left_hand_str = str(self.left_hand)
        if self.right_hand == -1:
            right_hand_str = "Right hand is out"
        else:
            right_hand_str = str(self.right_hand)
        return f"Player {self.player_name}: Left hand: {left_hand_str}, Right hand: {right_hand_str}"

    # method to check if the game is over
    def is_game_lost(self):
        return self.left_hand == 0 and self.right_hand == 0

    # method to react to a turn
    def touch_hand(self, hand, number_of_fingers):
        if hand == "left" and number_of_fingers >= 0:
            self.left_hand += number_of_fingers
        elif hand == "right" and number_of_fingers >= 0:
            self.right_hand += number_of_fingers
        else:
            raise ValueError("Invalid hand or number of fingers")
        if self.left_hand >= 5:
            self.left_hand = -1
        if self.right_hand >= 5:
            self.right_hand = -1


# %%
# main loop to play the game
player1 = Hands(1, 1, "Player 1")
player2 = Hands(1, 1, "Player 2")
turn_count = 0
while not (player1.is_game_lost() or player2.is_game_lost()):
    turn_count += 1
    print(f"Turn {turn_count}")
    # Player 1's turn
    print("Player 1's turn")
    print(player1)
    print(player2)
    # randomly choose a hand and number of fingers
    opponent_hand_to_touch = random.choice(["left", "right"])
    opponent_free_fingers = 5 - (
        player2.left_hand if opponent_hand_to_touch == "left" else player2.right_hand
    )
    number_of_fingers = random.randint(1, opponent_free_fingers)
    print(
        f"Player 1 touches {opponent_hand_to_touch} hand with {number_of_fingers} fingers"
    )
    player2.touch_hand(opponent_hand_to_touch, number_of_fingers)
    if player2.is_game_lost():
        print("Player 1 wins!")
        break
    # Player 2's turn
    print("Player 2's turn")
    print(player1)
    print(player2)
    # randomly choose a hand and number of fingers
    opponent_hand_to_touch = random.choice(["left", "right"])
    opponent_free_fingers = 5 - (
        player1.left_hand if opponent_hand_to_touch == "left" else player1.right_hand
    )
    number_of_fingers = random.randint(1, opponent_free_fingers)
    print(
        f"Player 2 touches {opponent_hand_to_touch} hand with {number_of_fingers} fingers"
    )
    player1.touch_hand(opponent_hand_to_touch, number_of_fingers)
    if player1.is_game_lost():
        print("Player 2 wins!")
        break


print("Game over")
if player1.is_game_lost():
    print(f"Player 1 lost, Player 2 wins! in {turn_count} turns")
elif player2.is_game_lost():
    print(f"Player 2 lost, Player 1 wins! in {turn_count} turns")


# %%
