import tkinter as tk
import random

class RussianNounTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Russian Noun Declensions Tester")
        
        self.nouns = [
            ("стол", "столом"),
            ("ручка", "ручкой"),
            ("мальчик", "мальчиком"),
            ("девочка", "девочкой"),
            ("дом", "домом"),
            ("книга", "книгой"),
            ("учитель", "учителем"),
            ("ученица", "ученицей"),
            ("яблоко", "яблоком"),
            ("дерево", "деревом")
        ]
        
        self.current_noun = None
        
        self.noun_label = tk.Label(root, text="", font=("Arial", 24))
        self.noun_label.pack(pady=20)
        
        self.entry = tk.Entry(root, font=("Arial", 24))
        self.entry.pack(pady=20)
        
        self.check_button = tk.Button(root, text="Check", command=self.check_answer, font=("Arial", 16))
        self.check_button.pack(pady=20)
        
        self.feedback_label = tk.Label(root, text="", font=("Arial", 16))
        self.feedback_label.pack(pady=20)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_noun, font=("Arial", 16))
        self.next_button.pack(pady=20)
        
        self.next_noun()
    
    def next_noun(self):
        self.current_noun, self.correct_form = random.choice(self.nouns)
        self.noun_label.config(text=self.current_noun)
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")
    
    def check_answer(self):
        user_input = self.entry.get().strip()
        if user_input == self.correct_form:
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(text=f"Incorrect! The correct form is '{self.correct_form}'", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = RussianNounTester(root)
    root.mainloop()
