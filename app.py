import tkinter as tk
from tkinter import messagebox
from calculator import add, subtract

def calculate():
    """Read input values, perform the selected operation, and show the result"""
    try:
        first_number = float(first_entry.get())
        second_number = float(second_entry.get())

        if operation.get() == "+":
            result = add(first_number, second_number)
        else:
            result = subtract(first_number, second_number)

        result_label.config(text=f"Результат: {result:g}")

    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")


root = tk.Tk()
root.title("Простой калькулятор")
root.geometry("320x300")
root.resizable(False, False)

title_label = tk.Label(root, text="Калькулятор", font=("Arial", 16))
title_label.pack(pady=10)

first_label = tk.Label(root, text="Первое число:")
first_label.pack()

first_entry = tk.Entry(root)
first_entry.pack(pady=5)

second_label = tk.Label(root, text="Второе число:")
second_label.pack()

second_entry = tk.Entry(root)
second_entry.pack(pady=5)

operation = tk.StringVar(value="+")

operations_frame = tk.Frame(root)
operations_frame.pack(pady=5)

add_radio = tk.Radiobutton(
    operations_frame,
    text="Сложение (+)",
    variable=operation,
    value="+",
)
add_radio.pack(side=tk.LEFT, padx=5)

subtract_radio = tk.Radiobutton(
    operations_frame,
    text="Вычитание (-)",
    variable=operation,
    value="-",
)
subtract_radio.pack(side=tk.LEFT, padx=5)

calculate_button = tk.Button(root, text="Вычислить", command=calculate)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="Результат:", font=("Arial", 12))
result_label.pack(pady=5)

root.mainloop()
