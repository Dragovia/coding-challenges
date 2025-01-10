import tkinter as tk
from tkinter import messagebox


def is_fibonacci_number(n):
    """
    Check if a number is in the Fibonacci sequence.
    A number is Fibonacci if and only if one of (5*n^2 + 4) or (5*n^2 - 4) is a perfect square.
    """
    if n < 0:
        return False

    def is_perfect_square(x):
        s = int(x ** 0.5)
        return s * s == x

    return is_perfect_square(5 * n ** 2 + 4) or is_perfect_square(5 * n ** 2 - 4)


def check_fibonacci():
    """Event handler to check if input is a Fibonacci number."""
    try:
        user_input = int(entry.get())
        if is_fibonacci_number(user_input):
            result_label.config(text=f"{user_input} is a Fibonacci number!", fg="green")
        else:
            result_label.config(text=f"{user_input} is NOT a Fibonacci number.", fg="red")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")


# Create the main application window
app = tk.Tk()
app.title("Fibonacci Checker")
app.geometry("400x200")
app.resizable(False, False)

# Create a label for instructions
instruction_label = tk.Label(app, text="Enter a number to check if it's in the Fibonacci sequence:", font=("Arial", 12))
instruction_label.pack(pady=10)

# Create an entry widget for user input
entry = tk.Entry(app, font=("Arial", 14))
entry.pack(pady=5)

# Create a button to trigger the check
check_button = tk.Button(app, text="Check", font=("Arial", 12), command=check_fibonacci)
check_button.pack(pady=10)

# Create a label to display results
result_label = tk.Label(app, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Run the application
app.mainloop()