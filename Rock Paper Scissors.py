import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

# Function to update the game state
def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)

    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1

    user_choice_label.config(text=f"User Choice: {user_choice}", fg="blue")
    computer_choice_label.config(text=f"Computer Choice: {computer_choice}", fg="red")
    result_label.config(text=result, fg="green" if result == "You win!" else "red" if result == "You lose!" else "orange")
    score_label.config(text=f"User Score: {user_score}  Computer Score: {computer_score}", fg="purple")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="User Choice: ", fg="black")
    computer_choice_label.config(text="Computer Choice: ", fg="black")
    result_label.config(text="", fg="black")
    score_label.config(text=f"User Score: {user_score}  Computer Score: {computer_score}", fg="purple")

# Setting up the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

choices = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0

# Creating widgets
user_choice_label = tk.Label(root, text="User Choice: ", font=("Arial", 14), fg="black")
computer_choice_label = tk.Label(root, text="Computer Choice: ", font=("Arial", 14), fg="black")
result_label = tk.Label(root, text="", font=("Arial", 16), fg="black")
score_label = tk.Label(root, text=f"User Score: {user_score}  Computer Score: {computer_score}", font=("Arial", 14), fg="purple")

rock_button = tk.Button(root, text="Rock", command=lambda: play('rock'))
paper_button = tk.Button(root, text="Paper", command=lambda: play('paper'))
scissors_button = tk.Button(root, text="Scissors", command=lambda: play('scissors'))
reset_button = tk.Button(root, text="Reset Game", command=reset_game)

# Placing widgets
user_choice_label.grid(row=0, column=0, padx=20, pady=20)
computer_choice_label.grid(row=0, column=1, padx=20, pady=20)
result_label.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
score_label.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

rock_button.grid(row=3, column=0, pady=10)
paper_button.grid(row=3, column=1, pady=10)
scissors_button.grid(row=4, column=0, pady=10)
reset_button.grid(row=4, column=1, pady=10)

# Running the main event loop
root.mainloop()

