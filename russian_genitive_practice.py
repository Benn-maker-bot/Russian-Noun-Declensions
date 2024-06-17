import tkinter as tk
from tkinter import messagebox

# Data for nouns and their genitive forms
nouns = {
    "дом": "дома",
    "мать": "матери",
    "сын": "сына",
    "яблоко": "яблока",
    "стол": "стола"
}

# Iterator for the current noun
current_noun_iter = iter(nouns.items())
current_noun = next(current_noun_iter)

def check_answer():
    user_answer = answer_entry.get()
    correct_answer = current_noun[1]
    
    if user_answer.strip().lower() == correct_answer:
        result_label.config(text="Correct!", fg="green")
    else:
        result_label.config(text=f"Incorrect. The correct form is: {correct_answer}", fg="red")
    
    # Move to the next noun
    next_noun()

def next_noun():
    global current_noun
    try:
        current_noun = next(current_noun_iter)
    except StopIteration:
        messagebox.showinfo("End", "You've completed all exercises!")
        root.destroy()
        return

    noun_label.config(text=current_noun[0])
    answer_entry.delete(0, tk.END)
    result_label.config(text="")

# Setting up the main window
root = tk.Tk()
root.title("Russian Genitive Case Practice")

noun_label = tk.Label(root, text=current_noun[0], font=("Arial", 14))
noun_label.pack(pady=10)

answer_entry = tk.Entry(root, font=("Arial", 14))
answer_entry.pack(pady=10)

check_button = tk.Button(root, text="Check", command=check_answer, font=("Arial", 14))
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Start the main event loop
root.mainloop()
