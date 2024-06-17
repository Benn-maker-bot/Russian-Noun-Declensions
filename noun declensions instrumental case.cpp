#include <iostream>
#include <string>
#include <vector>
#include <map>

// Function to display a menu and get user choice
int displayMenu() {
    int choice;
    std::cout << "Welcome to the Russian Grammar Exercises Program\n";
    std::cout << "1. Noun Declensions - Instrumental Case\n";
    std::cout << "2. Exit\n";
    std::cout << "Enter your choice: ";
    std::cin >> choice;
    return choice;
}

// Function to handle noun declensions exercise in the instrumental case
void nounDeclensionsInstrumentalExercise() {
    // Example nouns and their declensions in the instrumental case
    std::map<std::string, std::string> nouns = {
        {"стол", "столом"},
        {"окно", "окном"},
        {"учитель", "учителем"}
    };

    // Exercise logic here
    std::cout << "Noun Declensions - Instrumental Case Exercise\n";
    
    for (const auto& pair : nouns) {
        std::string answer;
        std::cout << "What is the instrumental case of '" << pair.first << "'? ";
        std::cin >> answer;
        
        if (answer == pair.second) {
            std::cout << "Correct!\n";
        } else {
            std::cout << "Incorrect. The correct answer is '" << pair.second << "'.\n";
        }
    }
}

int main() {
    int choice;
    
    while ((choice = displayMenu()) != 2) {
        switch (choice) {
            case 1:
                nounDeclensionsInstrumentalExercise();
                break;
            default:
                std::cout << "Invalid choice. Please try again.\n";
        }
    }

    std::cout << "Thank you for using the Russian Grammar Exercises Program.\n";

    return 0;
}
