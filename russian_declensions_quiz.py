import tkinter as tk
from tkinter import ttk, messagebox

# Predefined nouns with their declensions
nouns = {
    'masculine': {
        'стол': {'nominative_singular': 'стол', 'genitive_singular': 'стола', 'dative_singular': 'столу',
                 'accusative_singular': 'стол', 'instrumental_singular': 'столом', 'prepositional_singular': 'столе',
                 'nominative_plural': 'столы', 'genitive_plural': 'столов', 'dative_plural': 'столам',
                 'accusative_plural': 'столы', 'instrumental_plural': 'столами', 'prepositional_plural': 'столах'},
        # Add more masculine nouns
    },
    'feminine': {
        'книга': {'nominative_singular': 'книга', 'genitive_singular': 'книги', 'dative_singular': 'книге',
                  'accusative_singular': 'книгу', 'instrumental_singular': 'книгой', 'prepositional_singular': 'книге',
                  'nominative_plural': 'книги', 'genitive_plural': 'книг', 'dative_plural': 'книгам',
                  'accusative_plural': 'книги', 'instrumental_plural': 'книгами', 'prepositional_plural': 'книгах'},
        # Add more feminine nouns
    },
    'neuter': {
        'море': {'nominative_singular': 'море', 'genitive_singular': 'моря', 'dative_singular': 'морю',
                 'accusative_singular': 'море', 'instrumental_singular': 'морем', 'prepositional_singular': 'море',
                 'nominative_plural': 'моря', 'genitive_plural': 'морей', 'dative_plural': 'морям',
                 'accusative_plural': 'моря', 'instrumental_plural': 'морями', 'prepositional_plural': 'морях'},
        # Add more neuter nouns
    }
}

cases = ['nominative_singular', 'genitive_singular', 'dative_singular', 'accusative_singular', 'instrumental_singular', 'prepositional_singular',
         'nominative_plural', 'genitive_plural', 'dative_plural', 'accusative_plural', 'instrumental_plural', 'prepositional_plural']

class RussianDeclensionsQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Russian Noun Declensions Quiz")

        self.create_widgets()

    def create_widgets(self):
        self.noun_label = tk.Label(self.root, text="Select Noun:")
        self.noun_label.grid(row=0, column=0, padx=10, pady=10)

        self.noun_var = tk.StringVar()
        self.noun_combobox = ttk.Combobox(self.root, textvariable=self.noun_var)
        self.noun_combobox.grid(row=0, column=1, padx=10, pady=10)
        self.noun_combobox['values'] = [noun for gender in nouns.values() for noun in gender.keys()]

        self.case_label = tk.Label(self.root, text="Select Case:")
        self.case_label.grid(row=1, column=0, padx=10, pady=10)

        self.case_var = tk.StringVar()
        self.case_combobox = ttk.Combobox(self.root, textvariable=self.case_var)
        self.case_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.case_combobox['values'] = cases

        self.check_button = tk.Button(self.root, text="Check", command=self.check_declension)
        self.check_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_quiz)
        self.reset_button.grid(row=4, column=0, padx=10, pady=10)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.grid(row=4, column=1, padx=10, pady=10)

    def get_declension(self, noun, case):
        for gender, nouns_dict in nouns.items():
            if noun in nouns_dict:
                return nouns_dict[noun].get(case, "Declension not found")
        return "Noun not found"

    def check_declension(self):
        noun = self.noun_var.get()
        case = self.case_var.get()
        if noun and case:
            declension = self.get_declension(noun, case)
            self.result_label.config(text=f"{noun} in {case}: {declension}")
        else:
            messagebox.showwarning("Input Error", "Please select both a noun and a case.")

    def reset_quiz(self):
        self.noun_var.set("")
        self.case_var.set("")
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = RussianDeclensionsQuiz(root)
    root.mainloop()
