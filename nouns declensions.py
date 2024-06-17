# A simple Python program to provide grammar exercises for noun declensions in the instrumental case of the Russian language

nouns = {
    'стол': 'столом',
    'окно': 'окном',
    'учитель': 'учителем',
    # Add more nouns and their instrumental case here
}

def get_user_input(noun):
    return input(f"What is the instrumental case of '{noun}'? ").strip()

def check_answer(noun, user_input):
    correct_answer = nouns[noun]
    if user_input.lower() == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is '{correct_answer}'.")

def main():
    print("Russian Grammar Exercises - Instrumental Case")
    for noun in nouns:
        user_input = get_user_input(noun)
        check_answer(noun, user_input)

if __name__ == "__main__":
    main()
