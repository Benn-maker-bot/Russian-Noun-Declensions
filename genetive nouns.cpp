#include <windows.h>
#include <string>
#include <vector>
#include <map>

// Function declarations
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
void CheckAnswer(HWND hwnd);

// Data for nouns and their genitive forms
std::map<std::string, std::string> nouns = {
    {"дом", "дома"},
    {"мать", "матери"},
    {"сын", "сына"},
    {"яблоко", "яблока"},
    {"стол", "стола"}
};

std::map<std::string, std::string>::iterator currentNoun;

int WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, PWSTR pCmdLine, int nCmdShow) {
    const wchar_t CLASS_NAME[] = L"RussianGenitiveCasePractice";

    WNDCLASS wc = {};
    wc.lpfnWndProc = WindowProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = CLASS_NAME;

    RegisterClass(&wc);

    HWND hwnd = CreateWindowEx(
        0,
        CLASS_NAME,
        L"Russian Language Genitive Case Practice",
        WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, CW_USEDEFAULT, 500, 200,
        nullptr,
        nullptr,
        hInstance,
        nullptr
    );

    if (hwnd == nullptr) {
        return 0;
    }

    ShowWindow(hwnd, nCmdShow);

    MSG msg = {};
    while (GetMessage(&msg, nullptr, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}

LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    static HWND hNounStatic, hAnswerEdit, hCheckButton, hResultStatic;

    switch (uMsg) {
    case WM_CREATE: {
        hNounStatic = CreateWindow(L"STATIC", L"", WS_VISIBLE | WS_CHILD, 20, 20, 200, 20, hwnd, nullptr, nullptr, nullptr);
        hAnswerEdit = CreateWindow(L"EDIT", L"", WS_VISIBLE | WS_CHILD | WS_BORDER, 20, 50, 200, 20, hwnd, nullptr, nullptr, nullptr);
        hCheckButton = CreateWindow(L"BUTTON", L"Check", WS_VISIBLE | WS_CHILD, 20, 80, 80, 30, hwnd, (HMENU)1, nullptr, nullptr);
        hResultStatic = CreateWindow(L"STATIC", L"", WS_VISIBLE | WS_CHILD, 20, 120, 400, 20, hwnd, nullptr, nullptr, nullptr);

        currentNoun = nouns.begin();
        SetWindowTextA(hNounStatic, currentNoun->first.c_str());
        break;
    }
    case WM_COMMAND: {
        if (LOWORD(wParam) == 1) {
            CheckAnswer(hwnd);
        }
        break;
    }
    case WM_DESTROY: {
        PostQuitMessage(0);
        break;
    }
    default:
        return DefWindowProc(hwnd, uMsg, wParam, lParam);
    }
    return 0;
}

void CheckAnswer(HWND hwnd) {
    char answer[100];
    GetWindowTextA(GetDlgItem(hwnd, 2), answer, 100);

    std::string correctAnswer = currentNoun->second;
    std::string userAnswer = answer;

    if (userAnswer == correctAnswer) {
        SetWindowTextA(GetDlgItem(hwnd, 4), "Correct!");
    } else {
        std::string result = "Incorrect. The correct form is: " + correctAnswer;
        SetWindowTextA(GetDlgItem(hwnd, 4), result.c_str());
    }

    // Move to the next noun
    currentNoun++;
    if (currentNoun == nouns.end()) {
        currentNoun = nouns.begin();
    }

    SetWindowTextA(GetDlgItem(hwnd, 1), currentNoun->first.c_str());
    SetWindowTextA(GetDlgItem(hwnd, 2), "");
}
