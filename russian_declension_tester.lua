import tkinter as tk
from tkinter import messagebox
import random

# Sample data structure for Russian noun declensions
noun_declensions = {
    "собака": {
        "singular": {
            "nominative": "собака",
            "genitive": "собаки",
            "dative": "собаке",
            "accusative": "собаку",
            "instrumental": "собакой",
            "prepositional": "собаке"
        },
        "plural": {
            "nominative": "собаки",
            "genitive": "собак",
            "dative": "собакам",
            "accusative": "собак",
            "instrumental": "собаками",
            "prepositional": "собаках"
        }
    },
    # Add more nouns and their declensions here
}

cases = ["nominative", "genitive", "dative", "accusative", "instrumental", "prepositional"]
numbers = ["singular", "plural"]

# Initialize main window
root = tk.Tk()
root.title("Russian Noun Declension Tester")

# Variables to hold current question and user answer
current_noun = tk.StringVar()
current_case = tk.StringVar()
current_number = tk.StringVar()
user_answer = tk.StringVar()

def new_question():
    noun = random.choice(list(noun_declensions.keys()))
    number = random.choice(numbers)
    case = random.choice(cases)

    current_noun.set(noun)
    current_case.set(case)
    current_number.set(number)

    question_label.config(text=f"Decline '{noun}' in {number} {case} case:")
    answer_entry.delete(0, tk.END)

def check_answer():
    noun = current_noun.get()
    case = current_case.get()
    number = current_number.get()
    correct_answer = noun_declensions[noun][number][case]
    user_answer = answer_entry.get()

    if user_answer.strip() == correct_answer:
        messagebox.showinfo("Result", "Correct!")
    else:
        messagebox.showinfo("Result", f"Incorrect! The correct answer is '{correct_answer}'.")

# GUI components
question_label = tk.Label(root, text="", font=("Helvetica", 14))
question_label.pack(pady=10)

answer_entry = tk.Entry(root, textvariable=user_answer, font=("Helvetica", 14))
answer_entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit Answer", command=check_answer, font=("Helvetica", 14))
submit_button.pack(pady=10)

new_question_button = tk.Button(root, text="New Question", command=new_question, font=("Helvetica", 14))
new_question_button.pack(pady=10)

# Start with a new question
new_question()

# Run the application
root.mainloop()
