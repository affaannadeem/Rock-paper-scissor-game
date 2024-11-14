import tkinter as tk
import random

def play_game():
    user_choice = user_choice_var.get()
    computer_choice = random.choice(["rock", "paper", "scissors"])

    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}")

    if user_choice == computer_choice:
        result_label.config(text=f"It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            result_label.config(text="You win!")
        else:
            result_label.config(text="Computer wins!")
    elif user_choice == "paper":
        if computer_choice == "rock":
            result_label.config(text="You win!")
        else:
            result_label.config(text="Computer wins!")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            result_label.config(text="You win!")
        else:
            result_label.config(text="Computer wins!")
    else:
        result_label.config(text="Invalid input. Please enter rock, paper, or scissors.")

# Create the main window
window = tk.Tk()
window.title("Rock Paper Scissors")

# Create labels and buttons
user_choice_label = tk.Label(window, text="Enter your choice:")
user_choice_label.pack()

user_choice_var = tk.StringVar()
user_choice_entry = tk.Entry(window, textvariable=user_choice_var)
user_choice_entry.pack()

play_button = tk.Button(window, text="Play", command=play_game)
play_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()