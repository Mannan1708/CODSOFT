import random
import tkinter as tk
from tkinter import messagebox

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def program():
   try:
    total_letters = int(first.get())
    total_symbols = int(second.get())
    total_numbers = int(third.get())
    len = int(four.get())
    password_list = []

    for char in range(1, total_letters + 1):
      password_list.append(random.choice(letters))

    for char in range(1, total_symbols + 1):    
      password_list += random.choice(symbols)

    for char in range(1, total_numbers + 1):
      password_list += random.choice(numbers)

    random.shuffle(password_list)
    print(password_list)
    print(len)

    password = ""
    for char in password_list:
      password += char

    res.config(text=f"Password is {password}")
    ans.config(text=f"Total Length: {len}")

   except ValueError:
     messagebox.showerror("enter valid number")
     

start = tk.Tk()
start.title("Password Generator")

tk.Label(start, text="Total Length:").grid(row=0, column=0)
tk.Label(start, text="Letters:").grid(row=1, column=0)
tk.Label(start, text="Symbols:").grid(row=2, column=0)
tk.Label(start, text="Numbers:").grid(row=3, column=0)

four = tk.Entry(start)
first = tk.Entry(start)
second = tk.Entry(start)
third = tk.Entry(start)

four.grid(row=0,column=1)
first.grid(row=1, column=1)
second.grid(row=2, column=1)
third.grid(row=3, column=1)


button = tk.Button(start, text="Submit",command=lambda: program())
button.grid(row=5, column=1)

res = tk.Label(start, text="Password is: ")
res.grid(row=6, column=0)

ans = tk.Label(start, text="Total Length: ")
ans.grid(row=0, column=0)

start.mainloop()