# File: CS112_A1_T2_Game3_20230562
# Purpose: subtract perfect squares from number of coins .The player who is able to leave only 1 coin for the other player wins the game.
# Author: Rawda Mohammed Abdelreheem
# ID:20230562
import math
import random

def random_generator():
     #random_generator function Generates random number of coins between 10 and 1000
     # returns the randomly generated number
    coins = random.randint(10, 1000)
    print("The game starts with {} coins.".format(coins))
    return coins

def move_validation(n: int, total: int) -> bool:
    # move_validation Checks if the move is valid
    if not 0 < n < total:
        return False
    #  perfect square checker 
    return n == math.isqrt(n) ** 2 and n > 0

def game3(total: int) -> int:
    player = 1
#irritation to take moves  until the total number of coins is 0
    while total > 0:
        print("Player {}, enter your move (a non-zero square number less than {}): ".format(player, total))
        move = int(input())
        
        # Check if the move is valid
        if move_validation(move, total):
            # display the updated total number of coins and the current player number
            total -= move
            player = 3 - player
            # Check if the current player has won the game
            if total == 1:
                print("Player {} is the winner".format(player))
                break
        else:
            print("Invalid move, please try again.")

    return player

# display the menu for the user to choose how he wants to play 
print("*Subtract a Square Game Rules*")
print("Do you want to enter a number of coins or the program generates a number for you?")
print("A) Enter a number")
print("B) The program generates a number for you")

# take input of the number of coins available 
user_choice = input()
if user_choice.lower() == 'a' :
    while True :
         #validation of the user's input to ensure no strings are accepted        
        try: 
            total_coins = int(input("Enter the number of coins available to start the game: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
else :
    total_coins = random_generator()
    
print("Thank you for starting the game, now you have total coins of", total_coins)

winner = game3(total_coins)
print("congratulations")



