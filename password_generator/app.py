import tkinter as tk
from tkinter import messagebox, Frame
import random
import string

def generate():
    try:
        n = int(size.get())
        if n <= 0:
            raise ValueError("Enter only positive numbers")
    except ValueError as e:
        messagebox.showerror("Try again", str(e))
        return

    char = ""

    # Include ASCII letters if the checkbox is selected both uppercase and lowercase
    if letters.get():
        char += string.ascii_letters

    # Include digits if the checkbox is selected
    if numbers.get():
        char += string.digits

    # Include symbols if the checkbox is selected
    if symbols.get():
        char += string.punctuation

    # Ensure at least one character type is selected
    if not char:
        messagebox.showerror("Cannot proceed", "Check at least one checkbox")
        return

    # Generate the password based on selected character types and desired length
    password = ''.join(random.choices(char, k=n))

    # Display the generated password in the result label
    result.config(text=password)

def copy():
    root.clipboard_clear()
    root.clipboard_append(result.cget("text"))

root = tk.Tk()
root.title("Password Generator")
root.geometry('700x500')
root.config(bg='#fdf0d5')

heading_label = tk.Label(root, text="GENERATE RANDOM PASSWORD", fg="#c1121f", bg="#fdf0d5", font=("Helvetica", 16, "bold"))
heading_label.pack(pady=80)

length_label = tk.Label(root, text="How many characters:", fg="#c1121f", bg="#fdf0d5")
length_label.pack()
size = tk.Entry(root)
size.pack()

letters = tk.BooleanVar(value=False)
L_Checked = tk.Checkbutton(root, text="Add Letters", variable=letters, fg="#c1121f", bg="#fdf0d5")
L_Checked.pack()

numbers = tk.BooleanVar()
N_Checked = tk.Checkbutton(root, text="Add Numbers", variable=numbers, fg="#c1121f", bg="#fdf0d5")
N_Checked.pack()

symbols = tk.BooleanVar()
S_Checked = tk.Checkbutton(root, text="Add Symbols", variable=symbols, fg="#c1121f", bg="#fdf0d5")
S_Checked.pack()

button_f = Frame(root, bg="#fdf0d5")
button_f.pack(pady=20)

Generate = tk.Button(button_f, text="Generate", command=generate, bg="#c1121f", fg="white")
Generate.grid(row=0, column=0, padx=10)

Clipper = tk.Button(button_f, text="Copy", command=copy, bg="#c1121f", fg="white")
Clipper.grid(row=0, column=1, padx=10)

result = tk.Label(root, text="", fg="#c1121f", bg="#fdf0d5", font=("Helvetica", 14))
result.pack(pady=15)

root.mainloop()
