import random
import tkinter as tk
from tkinter import messagebox

Rock = '''
    _____
--'  ____)
     (_____)
     (_____)
     (____)
--._(___)
'''
Paper = '''
    ______
--'   ____)____
          _____)
         ______)
         ______)
--._________)
'''
Scissors = '''
    ______
--'   ____)___
         _____)
       ________)
      (____)
--.__(___)
'''
Game = [Rock, Paper, Scissors]
user_score = 0
computer_score = 0
def rps():
    try:
        user_choice = int(first.get())
        print(Game[user_choice])
        choice.config(text=f"Users Choise {Game[user_choice]}")

        computer_choice = random.randint(0, 2)
        print("Computer choose:")
        print(Game[computer_choice])
        choice_1.config(text=f"Computers Choise {Game[computer_choice]}")

        if user_choice >= 3 or user_choice < 0: 
            ans.config(text="You typed an invalid number.") 
        elif user_choice == 0 and computer_choice == 2:
            ans.config(text="You win!")
        elif computer_choice == 0 and user_choice == 2:
            ans.config(text="You lose")
        elif computer_choice > user_choice:
            ans.config(text="You lose")
        elif user_choice > computer_choice:
            ans.config(text="You win!")
        elif computer_choice == user_choice:
            ans.config(text="It's a draw")        
              
    except ValueError:
        messagebox.showerror("enter valid number")
     

def score():
        
        if ans == "You win!":
            user_score += 1
        elif ans == "You lose":
            computer_score += 1  


start = tk.Tk()
start.title("Rock Paper Sesiors Game")

tk.Label(start, text="Type 0 for Rock, 1 for Paper or 2 for Scissors:").grid(row=0, column=0)

first = tk.Entry(start)
first.grid(row=0, column=1)

choice = tk.Label(start, text="Users Choise is: ")
choice.grid(row=2, column=0)

choice_1 = tk.Label(start, text="Comuters Choise is: ")
choice_1.grid(row=6, column=0)

button = tk.Button(start, text="Submit",command=lambda:rps())
button.grid(row=7, column=1)

ans = tk.Label(start, text="Result is: ")
ans.grid(row=8, column=0)

user_score = tk.Label(start, text=f"Scores You: ",command=score())
user_score.grid(row=9, column=0)

computer_score = tk.Label(start, text=f"Computer: ",command=score())
computer_score.grid(row=9, column=1)

start.mainloop()

