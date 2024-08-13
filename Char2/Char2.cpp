// Char2 v1.1
// Gibt ASCII-Zeichen aus
// Andrei Avkhimovich
// for fun \o/

#include <iostream>
#include <iomanip> // Fuer std::setw
#include <vector>

int main() {
    const int startASCII = 1;   // Start
    const int endASCII = 255;   // Ende

    const int columnWidth = 8;  // Breite jeder Spalte
    const int columns = 4;      // Anzahl der Spalten

    // Vektor fuer gefilterte Symbole
    std::vector<std::pair<int, char>> symbols;

    // Fuelle den Vektor mit Zeichen, ueberpringe 7, 8, 9, 10, 13 und 27
    for (int i = startASCII; i <= endASCII; ++i) {
        if (i == 7 || i == 8 || i == 9 || i == 10 || i == 13 || i == 27) continue;
        symbols.emplace_back(i, static_cast<char>(i));
    }

    // Berechne die Anzahl der benoetigten Zeilen
    int totalSymbols = symbols.size();
    int rows = (totalSymbols + columns - 1) / columns; // Aufrunden von totalSymbols / columns

    // Willkommensnachricht
    std::cout << " ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ \n";
    std::cout << "||A |||S |||C |||I |||I |||- |||T |||a |||b |||e |||l |||l |||e ||\n";
    std::cout << "||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__||\n";
    std::cout << "|/__\\|/__\\|/__\\|/__\\|/__\\|/__\\|/__\\|/__\\|/__\\|/__\\|/__\\|/__\\|/__\\|\n";
    std::cout << "                                                       char2 v1.1\n";
    std::cout << "\n";

    // Ausgabe der Tabelle
    for (int row = 0; row < rows; ++row) {
        for (int col = 0; col < columns; ++col) {
            int index = row + col * rows; // Berechne den Index
            if (index < symbols.size()) {
                std::cout << std::left << std::setw(columnWidth)
                    << symbols[index].first
                    << std::setw(columnWidth)
                    << symbols[index].second;
            }
            else {
                // Leere Zellen fuellen
                std::cout << std::left << std::setw(columnWidth)
                    << ""
                    << std::setw(columnWidth)
                    << "";
            }
        }
        std::cout << std::endl;
    }

    // Symbole ohne Nummern, getrennt durch Leerzeichen
    std::cout << "\n";
    for (const auto& symbol : symbols) {
        std::cout << symbol.second << ' ';
    }
    std::cout << std::endl;

    // Auf anykey warten
    std::cin.get();

    return 0;
}