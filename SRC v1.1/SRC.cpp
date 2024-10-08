// Some Random Calculator v1.1
// Andrei Avkhimovich
// for fun \o/

#include <iostream>
#include <string>
#include <cctype>
#include <cmath>
#include <stdexcept>

// Hilfsfunktionen
void skipWhitespace(const std::string& expr, size_t& pos) {
    while (pos < expr.size() && std::isspace(expr[pos])) {
        ++pos;
    }
}

double parseNumber(const std::string& expr, size_t& pos) {
    skipWhitespace(expr, pos);
    size_t start = pos;
    while (pos < expr.size() && (std::isdigit(expr[pos]) || expr[pos] == '.')) {
        ++pos;
    }
    if (start == pos) {
        throw std::runtime_error("Fehler: Ungultige Zahl");
    }
    try {
        return std::stod(expr.substr(start, pos - start));
    }
    catch (const std::invalid_argument&) {
        throw std::runtime_error("Fehler beim Parsen der Zahl");
    }
}

double parseParentheses(const std::string& expr, size_t& pos);

double parseFactor(const std::string& expr, size_t& pos) {
    double value = parseParentheses(expr, pos);

    while (pos < expr.size()) {
        skipWhitespace(expr, pos);
        char op = expr[pos];

        if (op == '^') {
            ++pos;
            double exponent = parseParentheses(expr, pos);
            value = std::pow(value, exponent);
        }
        else {
            break;
        }
    }

    return value;
}

double parseTerm(const std::string& expr, size_t& pos) {
    double value = parseFactor(expr, pos);

    while (pos < expr.size()) {
        skipWhitespace(expr, pos);
        char op = expr[pos];

        if (op == '*' || op == '/') {
            ++pos;
            double nextValue = parseFactor(expr, pos);
            if (op == '*') {
                value *= nextValue;
            }
            else if (op == '/') {
                if (nextValue == 0) {
                    throw std::runtime_error("Fehler: Division durch Null");
                }
                value /= nextValue;
            }
        }
        else {
            break;
        }
    }

    return value;
}

double parseExpression(const std::string& expr, size_t& pos) {
    double value = parseTerm(expr, pos);

    while (pos < expr.size()) {
        skipWhitespace(expr, pos);
        char op = expr[pos];

        if (op == '+' || op == '-') {
            ++pos;
            double nextValue = parseTerm(expr, pos);
            if (op == '+') {
                value += nextValue;
            }
            else if (op == '-') {
                value -= nextValue;
            }
        }
        else {
            break;
        }
    }

    return value;
}

// Verarbeitet Klammern
double parseParentheses(const std::string& expr, size_t& pos) {
    skipWhitespace(expr, pos);

    if (expr[pos] == '(') {
        ++pos; // '(' uberspringen
        double value = parseExpression(expr, pos);
        skipWhitespace(expr, pos);
        if (expr[pos] != ')') {
            throw std::runtime_error("Fehlende schliessende Klammer");
        }
        ++pos; // ')' uberspringen
        return value;
    }
    return parseNumber(expr, pos); // Hier wird parseNumber anstelle von parseFactor aufgerufen
}

int main() {

    // Willkommensnachricht
    std::cout 
        << " ____  ____  _      _____   ____  ____  _      ____  ____  _     \n"
        << "/ ___\\/  _ \\/ \\__/|/  __/  /  __\\/  _ \\/ \\  /|/  _ \\/  _ \\/ \\__/|\n"
        << "|    \\| / \\|| |\\/|||  \\    |  \\/|| / \\|| |\\ ||| | \\|| / \\|| |\\/||\n"
        << "\\___ || \\_/|| |  |||  /_   |    /| |-||| | \\||| |_/|| \\_/|| |  ||\n"
        << "\\____/\\____/\\_/  \\|\\____\\  \\_/\\_\\\\_/ \\|\\_/  \\|\\____/\\____/\\_/  \\|\n" 
        << "   ____  ____  _     ____  _     _     ____  _____  ____  ____     \n"
        << "  /   _\\/  _ \\/ \\   /   _\\/ \\ /\\/ \\   /  _ \\/__ __\\/  _ \\/  __\\    \n" 
        << "  |  /  | / \\|| |   |  /  | | ||| |   | / \\|  / \\  | / \\||  \\/|    \n"
        << "  |  \\__| |-||| |_\\/|  \\__| \\_/|| |_\\/| |-||  | |  | \\_/||    /    \n" 
        << "  \\____/\\_/ \\|\\____/\\____/\\____/\\____/\\_/ \\|  \\_/  \\____/\\_/\\_\\    \n"
        << "                                                   .version 1.1\n"
        << "Verfugbare Symbole: + - * / ^ ( )\n"
        << "Beispiel: 1 + 2 * (3 ^ 2) / 4\n"
        << "Geben Sie die Formel ein: ";

    std::string expr;
    std::getline(std::cin, expr);

    try {
        size_t pos = 0;
        double result = parseExpression(expr, pos);
        skipWhitespace(expr, pos);
        if (pos < expr.size()) {
            std::cerr << std::endl << "Fehler: Nicht alle Zeichen der Formel wurden verarbeitet" << std::endl << std::endl;
            return 1;
        }
        std::cout << std::endl << "Ergebnis: " << result << std::endl << std::endl;
    }
    catch (const std::exception& e) {
        std::cerr << std::endl << "Fehler: " << e.what() << std::endl << std::endl;
        return 1;
    }

    system("pause");
    return 0;
}
