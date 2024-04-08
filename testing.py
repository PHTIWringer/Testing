'''
# Challenge 1: Write a Python program that asks the user to input a number and then prints out a countdown from that number to 1.

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
    
# Challenge 2: Create a Python program that generates a list of 10 random numbers between 1 and 100 and then prints the list, the maximum number, and the minimum number.

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

# Challenge 3: Write a Python program that asks the user to input a string and then prints out the number of vowels and consonants in that string.

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

# Challenge 4: Create a Python program that simulates a simple banking system. The program should allow users to create a new bank account with an initial # deposit, make deposits, make withdrawals, and check the account balance.

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

# Challenge 5: Write a Python program that simulates a simple tic-tac-toe game for two players. The game should display the board in the console, take # turns for each player to input their moves, and check for a win or a tie after every move.

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

# Challenge 6: Create a Python program that simulates a basic text-based adventure game. The player starts with an initial health of 100 and is in a room # with two doors: one leads to a room with a monster, and the other leads to a room with a treasure.

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

#######################################################################################################################################################

# Challenge: Write a Python program that creates a simple calculator. The calculator should be able to perform basic arithmetic operations like addition, # subtraction, multiplication, and division based on user input.

# Here's a step-by-step guide on how you can build this:

# Prompt the User: Ask the user to enter two numbers and the operation they want to perform. The operations can be denoted by symbols (+, -, *, /) or # words (add, subtract, multiply, divide).

# Perform the Operation: Based on the user's input, perform the corresponding arithmetic operation. You can use if-else statements to handle the different operations.

# Display the Result: Show the result of the arithmetic operation to the user.

number_one = float(input("Enter the first number: "))
number_two = float(input("Enter the second number: "))
operations = input("Choose the operation (+, -, *, /): ")

if operations == '+':
    result = number_one + number_two
elif operations == '-':
    result = number_one - number_two
elif operations == '*':
    result = number_one * number_two
elif operations == '/':
    if number_two != 0:
        result = number_one / number_two
    else:
        result = "Error"
else:
    result = "Invalid operation selected."

print(f"Solution: {result}")

#######################################################################################################################################################

# Challenge 7: Write a Python program that asks the user to input a list of numbers (you can decide whether they should be integers or floats). Once the user is done entering numbers, the program should calculate and print the sum, average, maximum, and minimum of the numbers.

# Here's a breakdown of what you should do:

# Input Numbers: Prompt the user to enter a series of numbers. You can ask them to enter the numbers separated by spaces or to enter each number one by  one, pressing enter between each one. You'll need to decide when the user is done entering numbers (e.g., they could enter a special character like # 'done' or press enter without typing a number).

# Store Numbers: You'll need to store the numbers the user inputs in a list so you can perform calculations on them later.

# Calculate Sum, Average, Maximum, and Minimum: Once you have the list of numbers, calculate the sum, average (sum divided by the count of numbers), the maximum number, and the minimum number. Python provides built-in functions like sum(), max(), and min() that you'll find useful.

# Print Results: Finally, print out the results to the user

print("Please enter a list of numbers below.")

user_number_list = []

while True:
    user_number = input("Your Number: ")
    if user_number in ('', 'q', 'quit', 'e', 'end', 'exit'):
        break
    elif user_number.isdigit():
        user_number_list.append(int(user_number))
    else:
        print('Invalid entry, please try again or press enter to end the list')

if user_number_list:
    average = sum(user_number_list) / len(user_number_list)
    print("Average:", average)
else:
    print("No numbers entered, so no average.")

print("Sum:", sum(user_number_list))

if user_number_list:
    print("Max:", max(user_number_list))
    print("Min:", min(user_number_list))
else:
    print("No numbers entered, so no min or max.")


#######################################################################################################################################################

# Challenge 8: Write a Python program that converts a time given in hours and minutes into seconds. The program should ask the user to input hours and minutes separately, then calculate and print the total time in seconds.

# Here's a step-by-step guide to approach it:

# Input Hours and Minutes: Prompt the user to enter hours and then minutes. You need to ensure that the input can be converted to an integer. You might also want to handle cases where the user enters negative numbers or non-numeric values.

# Convert Time to Seconds: Once you have valid hours and minutes, convert the total time to seconds. Remember, there are 3600 seconds in an hour and 60 seconds in a minute.

# Display the Result: Show the user the total time in seconds.

print("Please enter times in hours/minutes below seperately.")

hours_num = int(input())
minutes_num = int(input())
seconds = 60

if hours_num < 0:
    print("Please enter a positive time")
else:
    hours_seconds = hours_num * (seconds * seconds)
    print("Hours to Seconds: ", hours_seconds)
if minutes_num < 0:
    print("Please enter a postive time.")
else:
    minutes_seconds = minutes_num * seconds
    print("Minutes to Seconds: ", minutes_seconds)
    
print(f"Total time in Seconds: ", hours_seconds + minutes_seconds)


#######################################################################################################################################################

# Challenge 9: Write a Python program that generates a dictionary where the keys are numbers between 1 and n (inclusive) and the values are the squares of the keys. The program should ask the user for the number n and then print the generated dictionary.

# For example, if the user enters 5, the output should be {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.

# Here are the steps to approach this challenge:

# Get User Input: Ask the user to provide the number n. Ensure that you handle the input properly, converting it to an integer and checking that it's a positive number.

# Generate the Dictionary: Use a loop to create the dictionary. The loop should iterate through numbers from 1 to n, and for each number, it should add an entry to the dictionary where the key is the number and the value is the square of the number.

# Print the Dictionary: Finally, print the dictionary to show the result to the user.

n = int(input("Enter a number: "))

squares_dict = {}

for i in range(1, n + 1):
    squares_dict[i] = i ** 2

print(squares_dict)


#######################################################################################################################################################

# Challenge 10: Write a Python program to find the largest number in a list without using built-in functions like max().

# Here are the steps you should follow:

# Create a List: First, define a list of numbers. You can hardcode this list in your program. For example, numbers = [3, 6, 2, 8, 4, 10].

# Initialize a Variable for the Largest Number: Create a variable to hold the largest number. You can initialize it with the first element of the list.

# Loop Through the List: Use a loop to iterate through the list. Compare each number with the current largest number. If you find a number that's larger, update the variable to hold this new number.

# Print the Largest Number: After the loop finishes, print out the largest number.

numbers_list = [1, 4, 7, 42, -2, 54, 5, 89, 54, 100, -85, 25, 125]

def max_num(lst):
    largest_num = lst[0]
    for i in lst:
        if i > largest_num:
            largest_num = i
    return largest_num

maximum_num = max_num(numbers_list)

print(maximum_num)


#######################################################################################################################################################

# Challenge 11: Write a Python program that finds the second largest number in a list. You should not use any built-in functions like sorted() or max(), and you should only iterate through the list once.

# Here's how you can approach this:

# Create a List: Define a list of numbers. For example, numbers = [10, 36, 54, 89, 12, 27].

# Initialize Two Variables: Create two variables, one to hold the largest number and another to hold the second largest number. You can initialize them with the first element and the second element, but make sure to assign them correctly based on their value.

# Loop Through the List: Iterate through the list starting from the second or third element (since you've already used the first one or two to initialize your variables). Compare each element with your largest and second largest numbers and update these variables as necessary.

# Print the Result: After completing the loop, print out the second largest number.

numbers = [1, 4, 7, 42, -2, 54, 5, 89, 54, 100, -85, 25, 125]

def second_max(lst):
    if lst[0] > lst[1]:
        largest_num, second_large_num = lst[0], lst[1]
    else:
        largest_num, second_large_num = lst[1], lst[0]

    for i in lst[2:]:
        if i > largest_num:
            second_large_num, largest_num = largest_num, i
        elif largest_num > i > second_large_num:
            second_large_num = i

    return second_large_num

num_two = second_max(numbers)
print(num_two)
'''

#######################################################################################################################################################

# Challenge 12: Write a Python program to merge two sorted lists into a single sorted list. You should not use any built-in Python sorting functions. The program should efficiently combine the two lists, maintaining the order, and then print the merged sorted list.

# Here's a step-by-step guide to approach it:

# Create Two Sorted Lists: Define two lists that are already sorted. For example, list1 = [1, 3, 5, 7] and list2 = [2, 4, 6, 8].

# Initialize Pointers: Create pointers (indexes) for each list. These will track your position as you iterate through the lists.

# Merge the Lists: Iterate through both lists simultaneously, comparing the elements at the current pointer position of each list. Append the smaller element to the merged list and move the pointer for that list. If one list is exhausted, append the remaining elements from the other list.

# Print the Merged List: After the loop completes, the merged list should be a single sorted list containing all the elements from both input lists. Print this merged list.

