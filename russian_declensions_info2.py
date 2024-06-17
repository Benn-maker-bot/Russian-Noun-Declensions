import tkinter as tk
from tkinter import ttk, messagebox

# Declension rules and examples
declension_info = {
    'masculine': {
        'nominative_singular': {
            'rule': 'The nominative singular form for masculine nouns usually ends in a consonant.',
            'examples': [
                'Это мой стол. (This is my table.)',
                'Большой дом находится на улице. (The big house is on the street.)'
            ]
        },
        'genitive_singular': {
            'rule': 'For the genitive singular form, masculine nouns usually add "а" or "я".',
            'examples': [
                'У меня нет стола. (I do not have a table.)',
                'Возле дома есть парк. (There is a park near the house.)'
            ]
        },
        # Add other cases with many sentences here
    },
    'feminine': {
        'nominative_singular': {
            'rule': 'The nominative singular form for feminine nouns usually ends in "а" or "я".',
            'examples': [
                'Это моя книга. (This is my book.)',
                'Красивая страна. (A beautiful country.)'
            ]
        },
        'genitive_singular': {
            'rule': 'For the genitive singular form, feminine nouns usually add "и" or "ы".',
            'examples': [
                'Нет книги на столе. (There is no book on the table.)',
                'У страны есть границы. (The country has borders.)'
            ]
        },
        # Add other cases with many sentences here
    },
    'neuter': {
        'nominative_singular': {
            'rule': 'The nominative singular form for neuter nouns usually ends in "о" or "е".',
            'examples': [
                'Море спокойное сегодня. (The sea is calm today.)',
                'Окно открыто. (The window is open.)'
            ]
        },
        'genitive_singular': {
            'rule': 'For the genitive singular form, neuter nouns usually add "а" or "я".',
            'examples': [
                'Нет моря в этом городе. (There is no sea in this city.)',
                'Около окна есть стол. (There is a table near the window.)'
            ]
        },
        # Add other cases with many sentences here
    }
}

cases = ['nominative_singular', 'genitive_singular', 'dative_singular', 'accusative_singular', 'instrumental_singular', 'prepositional_singular',
         'nominative_plural', 'genitive_plural', 'dative_plural', 'accusative_plural', 'instrumental_plural', 'prepositional_plural']

class RussianDeclensionsInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Russian Noun Declensions Information")

        self.create_widgets()

    def create_widgets(self):
        self.gender_label = tk.Label(self.root, text="Select Gender:")
        self.gender_label.grid(row=0, column=0, padx=10, pady=10)

        self.gender_var = tk.StringVar()
        self.gender_combobox = ttk.Combobox(self.root, textvariable=self.gender_var)
        self.gender_combobox.grid(row=0, column=1, padx=10, pady=10)
        self.gender_combobox['values'] = ['masculine', 'feminine', 'neuter']

        self.case_label = tk.Label(self.root, text="Select Case:")
        self.case_label.grid(row=1, column=0, padx=10, pady=10)

        self.case_var = tk.StringVar()
        self.case_combobox = ttk.Combobox(self.root, textvariable=self.case_var)
        self.case_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.case_combobox['values'] = cases

        self.show_button = tk.Button(self.root, text="Show", command=self.show_info)
        self.show_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.info_text = tk.Text(self.root, wrap=tk.WORD, width=60, height=20)
        self.info_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_selection)
        self.reset_button.grid(row=4, column=0, padx=10, pady=10)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.grid(row=4, column=1, padx=10, pady=10)

    def get_info(self, gender, case):
        return declension_info.get(gender, {}).get(case, {"rule": "Information not available", "examples": ["Example not available"]})

    def show_info(self):
        gender = self.gender_var.get()
        case = self.case_var.get()
        if gender and case:
            info = self.get_info(gender, case)
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, f"Rule: {info['rule']}\n\nExamples:\n")
            for example in info['examples']:
                self.info_text.insert(tk.END, f"- {example}\n")
        else:
            messagebox.showwarning("Input Error", "Please select both a gender and a case.")

    def reset_selection(self):
        self.gender_var.set("")
        self.case_var.set("")
        self.info_text.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = RussianDeclensionsInfoApp(root)
    root.mainloop()
