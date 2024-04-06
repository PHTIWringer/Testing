'''
cents = int(input())

quarters = cents // 25
cents = cents % 25

dimes = cents // 10
cents = cents % 10

nickels = cents // 5
cents = cents % 5

pennies = cents

print("Change:")
print("Q:", quarters)
print("D:", dimes)
print("N:", nickels)
print("P:", pennies)

###################################################################################################################################################

# Challenge: Write a Python program that asks the user to input a number and then prints out a countdown from that number to 1.

# Here's what your program should do:

# Prompt the user to enter a number.
# Validate that the input is an integer and greater than 0. If not, prompt the user again.
# Print a countdown from the entered number down to 1.

print("Please enter a number:")
number = int(input())

if number > 0:
    while number > 0:
        print(number)
        number -= 1
elif number < 0:
    print("Please enter a number greater than 0")

#################################################################################################################################################
    
# Challenge: Create a Python program that generates a list of 10 random numbers between 1 and 100 and then prints the list, the maximum number, and the minimum number.

# Here's a breakdown of what your program should do:

# Import the random module to generate random numbers.
# Create an empty list to store your random numbers.
# Use a loop to generate 10 random numbers between 1 and 100 and append each number to the list.
# Print the list of random numbers.
# Use built-in functions to find and print the maximum and minimum numbers from the list.

from random import randint

random_number_list = []

for i in range(10):
    random_number_list.append((randint(1, 100)))

print(random_number_list)
print(max(random_number_list))
print(min(random_number_list))


##############################################################################################################################################

# Challenge: Write a Python program that asks the user to input a string and then prints out the number of vowels and consonants in that string.

# Here's a step-by-step breakdown of what your program should do:

# Prompt the user to enter a string.
# Initialize two counters, one for vowels and one for consonants.
# Loop through each character in the input string.
# Check if the current character is a vowel or a consonant. You can consider 'a', 'e', 'i', 'o', and 'u' (both uppercase and lowercase) as vowels, and # all other alphabetic characters as consonants.
# Increment the appropriate counter based on whether the character is a vowel or a consonant.
# After the loop, print out the counts for vowels and consonants.
# Keep in mind to handle the case sensitivity (i.e., 'A' and 'a' should both be counted as vowels) and ensure that non-alphabetic characters are not # counted.

print("Please enter a string: ")

def count_vowels(string):
    vowels = ('aeiou')
    count_vowel = 0
    for character in string.lower():
        if character in vowels:
            count_vowel += 1
    return count_vowel

def count_consonant(string):
    consonant = ('bcdfghjklmnpqrstvwxyz')
    count_consonant = 0
    for character in string.lower():
        if character in consonant:
            count_consonant += 1
    return count_consonant

user_input = input()
vowel = count_vowels(user_input)
consonant = count_consonant(user_input)

print(f"There are {vowel} vowels and {consonant} consonants in: '{user_input}'.")


#######################################################################################################################################################

# Challenge: Create a Python program that simulates a simple banking system. The program should allow users to create a new bank account with an initial # deposit, make deposits, make withdrawals, and check the account balance.

# Here are the specific requirements:

# Define a class called BankAccount with the following attributes:

# account_number: a unique identifier for the account (for simplicity, you can start this at 1 and increment for each new account).
# balance: the amount of money in the account.
# Within the BankAccount class, define the following methods:

# __init__(self, initial_balance): Initializes a new account with the provided initial_balance.
# deposit(self, amount): Adds the specified amount to the account balance.
# withdraw(self, amount): Subtracts the specified amount from the account balance if there are sufficient funds; if not, print an error message.
# get_balance(self): Prints the current balance of the account.
# Allow the user to interact with the program through the console. The user should be able to:

# Create a new account with an initial deposit amount.
# Make a deposit to their account.
# Make a withdrawal from their account.
# Check the account balance.
# You can simulate the user interaction within the console by using input() statements to capture user choices and perform the corresponding actions.

class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        print(f"Current balance: {self.balance}")

print("Welcome to the Simple Bank System!")
initial_deposit = float(input("Please enter an initial deposit: "))
account = BankAccount(initial_deposit)

while True:
    print("\nWhat would you like to do?")
    print("1: Deposit")
    print("2: Withdraw")
    print("3: Check Balance")
    print("4: Exit")
    choice = input("Please enter your choice (1-4): ")

    if choice == '1':
        amount = float(input("Enter the amount to deposit: "))
        account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter the amount to withdraw: "))
        account.withdraw(amount)
    elif choice == '3':
        account.get_balance()
    elif choice == '4':
        print("Thank you for using the Simple Bank System!")
        break
    else:
        print("Invalid choice, please choose again.")


#######################################################################################################################################################

# Challenge: Write a Python program that simulates a simple tic-tac-toe game for two players. The game should display the board in the console, take # turns for each player to input their moves, and check for a win or a tie after every move.

# Here's a detailed breakdown:

# Initialize the Board: Create a 3x3 board using a list of lists. You can represent empty spots with a number or a symbol like '-'.

# Display the Board: Write a function to print the board after each move. The board should be displayed in a way that shows the current state of the # game, with the players' moves updated.

# Player Moves: Alternately ask each player (Player 1 and Player 2) to select their spot on the board. You need to check if the chosen spot is valid # (within the board range and not already taken).

# Check for Win or Tie: After every move, check if there is a winner. A win is defined as three of the same symbols (X or O) in a row, column, or # diagonal. Also, check if the board is full and declare a tie if there are no empty spots left and no winner.

# Switch Turns: Alternate between players after each valid move.

# End Game: The game ends when there is a winner or a tie. Announce the result.

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    win = any(all(cell == player for cell in row) for row in board)  # Check rows
    win |= any(all(board[row][col] == player for row in range(3)) for col in range(3))  # Check columns
    win |= all(board[i][i] == player for i in range(3))  # Check diagonal
    win |= all(board[i][2 - i] == player for i in range(3))  # Check anti-diagonal
    return win

def check_tie(board):
    return all(all(cell in ['X', 'O'] for cell in row) for row in board)

def get_move(player):
    while True:
        position = input(f"{player}'s turn. Enter the position (1-9): ")
        if position.isdigit() and 1 <= int(position) <= 9:
            row, col = divmod(int(position) - 1, 3)
            if board[row][col] not in ['X', 'O']:
                return row, col
            else:
                print("This position is already taken. Please try again.")
        else:
            print("Invalid input. Please enter a number from 1 to 9.")

# Initialize the board
board = [[str(i + j * 3) for i in range(1, 4)] for j in range(3)]

# Game loop
current_player = "X"
while True:
    print_board(board)
    
    # Get current player's move
    row, col = get_move(current_player)
    board[row][col] = current_player
    
    # Check for win or tie
    if check_win(board, current_player):
        print_board(board)
        print(f"{current_player} wins!")
        break
    elif check_tie(board):
        print_board(board)
        print("It's a tie!")
        break
    
    # Switch players
    current_player = "O" if current_player == "X" else "X"



########################################################################################################################################################

# Challenge: Create a Python program that simulates a basic text-based adventure game. The player starts with an initial health of 100 and is in a room # with two doors: one leads to a room with a monster, and the other leads to a room with a treasure.

# Here's a breakdown of what your program should do:

# Introduction: Display a brief description of the game and the initial scenario. The player has two choices: door 1 or door 2.

# Choice: Ask the player to choose a door. Validate the input to ensure it's either 1 or 2.

# Consequences:

# If the player chooses the door with the monster, display a message about encountering the monster. The player loses a certain amount of health (you can # decide how much). Then, check if the player's health is greater than 0. If the player's health is 0 or less, they lose the game. If they still have # health left, they can choose to escape or fight.
# If the player chooses the door with the treasure, they win the game. Display a congratulatory message.
# Player Decisions: If the player encounters the monster and chooses to fight, decide the outcome of the fight randomly. The player can either defeat the # monster and win or lose the fight and the game.

# Ending: The game should provide a message based on the player's outcome (winning the treasure, defeating the monster, escaping, or losing to the # monster).

import random

def encounter_monster(health):
    print("You've encountered a monster!")
    action = input("Do you choose to fight (f) or escape (e)? ").lower()

    if action == 'f':
        # Simulate fight outcome
        if random.choice([True, False]):  # 50% chance to win
            print("You defeated the monster and found the treasure! You win!")
        else:
            print("You fought bravely but were defeated by the monster.")
            health = 0
    elif action == 'e':
        # Escape scenario
        print("You escaped back to the room. Unfortunately, there's nowhere else to go.")
        health -= 30  # Penalty for escaping
        if health > 0:
            print(f"You lost some health while escaping. Current health: {health}")
        else:
            print("You've lost all your health while escaping. Game over.")
    
    return health

def find_treasure():
    print("You found the treasure! Congratulations, you win!")

print("Welcome to the Adventure Game!")
print("You find yourself in a room with two doors. One leads to a monster, the other to a treasure.")
health = 100

while True:
    door_choice = input("Do you go through door 1 or door 2? Enter 1 or 2: ")
    if door_choice not in ['1', '2']:
        print("Invalid input. Please enter 1 or 2.")
        continue

    if door_choice == '1':
        health = encounter_monster(health)
        if health <= 0:
            print("You've lost all your health. Game over.")
            break
    else:
        find_treasure()
        break
'''