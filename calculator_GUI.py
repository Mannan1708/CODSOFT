import tkinter as tk
from tkinter import messagebox

def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Cannot divide by zero"

def calc(operations):
    try:
        n1 = float(first.get())
        n2 = float(second.get())
           
        if operations == "+":
            ans = addition(n1, n2)
        elif operations == "-":
            ans = subtraction(n1, n2)
        elif operations == "*":
            ans = multiplication(n1, n2)
        elif operations == "/":
            ans = division(n1, n2)
        
        res.config(text=f"Equals to: {ans}")
    except ValueError:
        messagebox.showerror("Enter valid numbers")

start = tk.Tk()
start.title("Simple Arithmetic Calculator")

tk.Label(start, text="First number:").grid(row=0, column=0)
tk.Label(start, text="Second number:").grid(row=1, column=0)

first = tk.Entry(start)
second = tk.Entry(start)

first.grid(row=0, column=1)
second.grid(row=1, column=1)

button = tk.Button(start, text="+",command=lambda: calc("+"))
button.grid(row=2, column=0)

button = tk.Button(start, text="-",command=lambda: calc("-"))
button.grid(row=2, column=1)

button = tk.Button(start, text="*",command=lambda: calc("*"))
button.grid(row=3, column=0)

button = tk.Button(start, text="/",command=lambda: calc("/"))
button.grid(row=3, column=1)

res = tk.Label(start, text="Equals to: ")
res.grid(row=6, column=1)

start.mainloop()