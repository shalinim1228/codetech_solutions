import tkinter as tk
from tkinter import messagebox

# Functions to perform the calculations
def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 + num2)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 - num2)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 * num2)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Math Error", "Cannot divide by zero.")
        else:
            result.set(num1 / num2)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Basic Calculator")

# Create StringVar to hold the result
result = tk.StringVar()

# Create input fields and labels
label1 = tk.Label(root, text="Enter first number:")
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Enter second number:")
label2.grid(row=1, column=0, padx=10, pady=10)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Create buttons for each operation
button_add = tk.Button(root, text="Add", width=10, command=add)
button_add.grid(row=2, column=0, padx=10, pady=10)

button_subtract = tk.Button(root, text="Subtract", width=10, command=subtract)
button_subtract.grid(row=2, column=1, padx=10, pady=10)

button_multiply = tk.Button(root, text="Multiply", width=10, command=multiply)
button_multiply.grid(row=3, column=0, padx=10, pady=10)

button_divide = tk.Button(root, text="Divide", width=10, command=divide)
button_divide.grid(row=3, column=1, padx=10, pady=10)

# Label to display the result
result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=0, padx=10, pady=10)

result_display = tk.Label(root, textvariable=result, width=15, height=2, relief="sunken")
result_display.grid(row=4, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
