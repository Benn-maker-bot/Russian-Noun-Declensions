import tkinter as tk

# Sample data structure for Russian noun declension rules and examples
declension_rules = {
    "nominative": {
        "singular": "The nominative case is used for the subject of the sentence.",
        "plural": "The nominative case is used for the subject of the sentence in plural."
    },
    "genitive": {
        "singular": "The genitive case is used to indicate possession, or absence of something.",
        "plural": "The genitive case is used to indicate possession, or absence of something in plural."
    },
    "dative": {
        "singular": "The dative case is used to indicate the indirect object of a verb.",
        "plural": "The dative case is used to indicate the indirect object of a verb in plural."
    },
    "accusative": {
        "singular": "The accusative case is used to indicate the direct object of a verb.",
        "plural": "The accusative case is used to indicate the direct object of a verb in plural."
    },
    "instrumental": {
        "singular": "The instrumental case is used to indicate the means by which an action is performed.",
        "plural": "The instrumental case is used to indicate the means by which an action is performed in plural."
    },
    "prepositional": {
        "singular": "The prepositional case is used to indicate location or topics of speech.",
        "plural": "The prepositional case is used to indicate location or topics of speech in plural."
    }
}

examples = {
    "nominative": {
        "singular": "собака (dog) - Собака лает. (The dog barks.)",
        "plural": "собаки (dogs) - Собаки лают. (The dogs bark.)"
    },
    "genitive": {
        "singular": "собаки (of the dog) - У меня нет собаки. (I don't have a dog.)",
        "plural": "собак (of the dogs) - У меня нет собак. (I don't have dogs.)"
    },
    "dative": {
        "singular": "собаке (to the dog) - Я дал еду собаке. (I gave food to the dog.)",
        "plural": "собакам (to the dogs) - Я дал еду собакам. (I gave food to the dogs.)"
    },
    "accusative": {
        "singular": "собаку (the dog) - Я вижу собаку. (I see the dog.)",
        "plural": "собак (the dogs) - Я вижу собак. (I see the dogs.)"
    },
    "instrumental": {
        "singular": "собакой (with the dog) - Я гуляю с собакой. (I walk with the dog.)",
        "plural": "собаками (with the dogs) - Я гуляю с собаками. (I walk with the dogs.)"
    },
    "prepositional": {
        "singular": "собаке (about the dog) - Я думаю о собаке. (I think about the dog.)",
        "plural": "собаках (about the dogs) - Я думаю о собаках. (I think about the dogs.)"
    }
}

# Initialize main window
root = tk.Tk()
root.title("Russian Noun Declension Rules")

# Function to display rules and examples
def display_info(case, number):
    rules_text.set(declension_rules[case][number])
    examples_text.set(examples[case][number])

# GUI components
rules_text = tk.StringVar()
examples_text = tk.StringVar()

# Labels
rules_label = tk.Label(root, text="Rules", font=("Helvetica", 14))
rules_label.pack(pady=5)

rules_display = tk.Label(root, textvariable=rules_text, wraplength=400, justify="left", font=("Helvetica", 12))
rules_display.pack(pady=5)

examples_label = tk.Label(root, text="Examples", font=("Helvetica", 14))
examples_label.pack(pady=5)

examples_display = tk.Label(root, textvariable=examples_text, wraplength=400, justify="left", font=("Helvetica", 12))
examples_display.pack(pady=5)

# Buttons for each case and number
for case in declension_rules.keys():
    case_frame = tk.Frame(root)
    case_frame.pack(pady=5)

    case_label = tk.Label(case_frame, text=case.capitalize(), font=("Helvetica", 12, "bold"))
    case_label.pack(side="left", padx=10)

    singular_button = tk.Button(case_frame, text="Singular", command=lambda c=case: display_info(c, "singular"))
    singular_button.pack(side="left", padx=5)

    plural_button = tk.Button(case_frame, text="Plural", command=lambda c=case: display_info(c, "plural"))
    plural_button.pack(side="left", padx=5)

# Run the application
root.mainloop()
