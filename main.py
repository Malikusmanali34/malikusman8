import random
import tkinter as tk
from tkinter import messagebox, simpledialog
import sys

class BoldMessageDialog(tk.Toplevel):
    def __init__(self, parent, title, message):
        super().__init__(parent)
        self.title(title)
        
        label = tk.Label(self, text=message, font=("Helvetica", 14, "bold"))
        label.pack(padx=20, pady=20)

        ok_button = tk.Button(self, text="OK", command=self.destroy)
        ok_button.pack(pady=10)

def guess_the_number():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Define the levels and their corresponding ranges
    levels = [
        {"level": 1, "max_number": 10},
        {"level": 2, "max_number": 15},
        {"level": 3, "max_number": 20},
        {"level": 4, "max_number": 25},
        {"level": 5, "max_number": 30}
    ]

    for level_data in levels:
        level = level_data["level"]
        max_number = level_data["max_number"]

        secret_number = random.randint(1, max_number)
        attempts = 0

        messagebox.showinfo("Welcome", f"Welcome to Level {level}!\nI'm thinking of a number between 1 and {max_number}.")

        while True:
            # Get the player's guess
            try:
                guess = int(tk.simpledialog.askstring(f"Level {level} - Guess the Number", "Your guess:"))
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number.")
                continue

            # Increment the attempts counter
            attempts += 1

            # Check if the guess is correct
            if guess == secret_number:
                dialog = BoldMessageDialog(root, "Congratulations!", f"You guessed the number in {attempts} attempts. Well done!")
                root.wait_window(dialog)  # Wait for the dialog to be closed before continuing
                break  # Move to the next level

            elif guess < secret_number:
                messagebox.showinfo("Too Low", "Too low. Try again.")
            else:
                messagebox.showinfo("Too High", "Too high. Try again.")

    messagebox.showinfo("Game Over", "Congratulations! You completed all levels. Well done!")
    sys.exit()

if __name__ == "__main__":
    guess_the_number()
