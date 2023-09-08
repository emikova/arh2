import tkinter as tk
import random

def play(user_choice):
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == 'Rock' and computer_choice == 'Scissors') or
        (user_choice == 'Paper' and computer_choice == 'Rock') or
        (user_choice == 'Scissors' and computer_choice == 'Paper')
    ):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Create buttons
rock_button = tk.Button(root, text="Rock", command=lambda: play('Rock'))
paper_button = tk.Button(root, text="Paper", command=lambda: play('Paper'))
scissors_button = tk.Button(root, text="Scissors", command=lambda: play('Scissors'))

# Create result label
result_label = tk.Label(root, text="Make your choice!")

# Grid layout for buttons and label
rock_button.grid(row=0, column=0)
paper_button.grid(row=0, column=1)
scissors_button.grid(row=0, column=2)
result_label.grid(row=1, column=0, columnspan=3)

# Start the main event loop
root.mainloop()
