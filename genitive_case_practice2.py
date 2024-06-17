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

class GenitiveCasePracticeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Russian Language Genitive Case Practice")

        self.current_noun = iter(nouns)
        self.noun_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.noun_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=("Helvetica", 16))
        self.answer_entry.pack(pady=10)

        self.check_button = tk.Button(root, text="Check", command=self.check_answer, font=("Helvetica", 16))
        self.check_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.result_label.pack(pady=20)

        self.next_noun()

    def next_noun(self):
        try:
            self.current_word = next(self.current_noun)
        except StopIteration:
            self.current_noun = iter(nouns)
            self.current_word = next(self.current_noun)
        self.noun_label.config(text=self.current_word)
        self.answer_entry.delete(0, tk.END)
        self.result_label.config(text="")

    def check_answer(self):
        user_answer = self.answer_entry.get()
        correct_answer = nouns[self.current_word]

        if user_answer == correct_answer:
            self.result_label.config(text="Correct!", fg="green")
        else:
            self.result_label.config(text=f"Incorrect. The correct form is: {correct_answer}", fg="red")
        
        self.next_noun()

if __name__ == "__main__":
    root = tk.Tk()
    app = GenitiveCasePracticeApp(root)
    root.mainloop()
