// XO .ein einfaches Tic-Tac-Toe-Spiel
// Andrei Avkhimovich
// Just for fun \o/

#include <iostream>
#include <vector>
#include <cstdlib>  // fur std::rand() und std::srand()
#include <ctime>    // fur std::time() zur Zufallszahlengenerierung
#include <limits>   // fur std::numeric_limits
#include <algorithm> // fur std::find

using namespace std;

// Funktion zum Drucken des Spielbretts
void printBoard(const vector<vector<char>>& board) {
    cout << endl << "  1 2 3\n";
    for (int i = 0; i < 3; ++i) {
        cout << i + 1 << ' ';
        for (int j = 0; j < 3; ++j) {
            cout << board[i][j] << ' ';
        }
        cout << endl;
    }
}

// Ueberpruefen, ob ein Spieler gewonnen hat
bool checkWin(const vector<vector<char>>& board, char player) {
    for (int i = 0; i < 3; ++i) {
        if ((board[i][0] == player && board[i][1] == player && board[i][2] == player) ||
            (board[0][i] == player && board[1][i] == player && board[2][i] == player)) {
            return true;
        }
    }

    return (board[0][0] == player && board[1][1] == player && board[2][2] == player) ||
        (board[0][2] == player && board[1][1] == player && board[2][0] == player);
}

// Ueberpruefen, ob das Brett voll ist
bool isBoardFull(const vector<vector<char>>& board) {
    for (const auto& row : board) {
        if (find(row.begin(), row.end(), ' ') != row.end()) {
            return false;
        }
    }
    return true;
}

// Minimax-Funktion zur Bewertung des besten Zuges
int minimax(vector<vector<char>>& board, bool isMaximizing, char player, char opponent) {
    if (checkWin(board, player)) return 10;
    if (checkWin(board, opponent)) return -10;
    if (isBoardFull(board)) return 0;

    if (isMaximizing) {
        int bestScore = std::numeric_limits<int>::min();
        for (int row = 0; row < 3; ++row) {
            for (int col = 0; col < 3; ++col) {
                if (board[row][col] == ' ') {
                    board[row][col] = player;
                    int score = minimax(board, false, player, opponent);
                    board[row][col] = ' ';
                    bestScore = std::max(score, bestScore);
                }
            }
        }
        return bestScore;
    }
    else {
        int bestScore = std::numeric_limits<int>::max();
        for (int row = 0; row < 3; ++row) {
            for (int col = 0; col < 3; ++col) {
                if (board[row][col] == ' ') {
                    board[row][col] = opponent;
                    int score = minimax(board, true, player, opponent);
                    board[row][col] = ' ';
                    bestScore = std::min(score, bestScore);
                }
            }
        }
        return bestScore;
    }
}

// Funktion, um den besten Zug fuer den Computer zu finden
void computerMove(vector<vector<char>>& board, char computerPlayer, char player, bool isHard, bool isFirstMove) {
    if (isFirstMove) {
        // Erster Zug: Zufallsgenerierter Zug
        int row, col;
        do {
            row = std::rand() % 3;
            col = std::rand() % 3;
        } while (board[row][col] != ' ');

        board[row][col] = computerPlayer;
        cout << endl << "Computer hat " << computerPlayer << " auf Position " << row + 1 << " " << col + 1 << " gesetzt." << endl;
    }
    else {
        if (isHard) {
            // Schwierigkeitsgrad ist schwer: Minimax-Algorithmus
            int bestScore = std::numeric_limits<int>::min();
            int bestRow = -1, bestCol = -1;

            for (int row = 0; row < 3; ++row) {
                for (int col = 0; col < 3; ++col) {
                    if (board[row][col] == ' ') {
                        board[row][col] = computerPlayer;
                        int score = minimax(board, false, computerPlayer, player);
                        board[row][col] = ' ';
                        if (score > bestScore) {
                            bestScore = score;
                            bestRow = row;
                            bestCol = col;
                        }
                    }
                }
            }

            board[bestRow][bestCol] = computerPlayer;
            cout << endl << "Computer hat " << computerPlayer << " auf Position " << bestRow + 1 << " " << bestCol + 1 << " gesetzt." << endl;
        }
        else {
            // Schwierigkeitsgrad ist einfach: Zufallsgenerierter Zug
            int row, col;
            do {
                row = std::rand() % 3;
                col = std::rand() % 3;
            } while (board[row][col] != ' ');

            board[row][col] = computerPlayer;
            cout << endl << "Computer hat " << computerPlayer << " auf Position " << row + 1 << " " << col + 1 << " gesetzt." << endl;
        }
    }
}

// Spielerzug verarbeiten
void playerMove(vector<vector<char>>& board, char player) {
    int row, col;
    do {
        cout << endl << "Spieler " << player << ", gib Zeile und Spalte ein (zb 1 2): ";
        cin >> row >> col;
        --row; --col;
    } while (row < 0 || row >= 3 || col < 0 || col >= 3 || board[row][col] != ' ');
    board[row][col] = player;
}

int main() {
    // Initialisierung des Zufallszahlengenerators
    std::srand(std::time(0));

    vector<vector<char>> board(3, vector<char>(3, ' '));
    char currentPlayer, opponentPlayer;
    int opponentChoice, difficultyChoice;

    // Willkommensnachricht
    std::cout
        << endl
        << " XXXXXXX       XXXXXXX     OOOOOOOOO\n"
        << " X:::::X       X:::::X   OO:::::::::OO\n"
        << " X:::::X       X:::::X OO:::::::::::::OO\n"
        << " X::::::X     X::::::XO:::::::OOO:::::::O\n"
        << " XXX:::::X   X:::::XXXO::::::O   O::::::O\n"
        << "    X:::::X X:::::X   O:::::O     O:::::O\n"
        << "     X:::::X:::::X    O:::::O     O:::::O\n"
        << "      X:::::::::X     O:::::O     O:::::O\n"
        << "      X:::::::::X     O:::::O     O:::::O\n"
        << "     X:::::X:::::X    O:::::O     O:::::O\n"
        << "    X:::::X X:::::X   O:::::O     O:::::O\n"
        << " XXX:::::X   X:::::XXXO::::::O   O::::::O\n"
        << " X::::::X     X::::::XO:::::::OOO:::::::O\n"
        << " X:::::X       X:::::X OO:::::::::::::OO\n"
        << " X:::::X       X:::::X   OO:::::::::OO\n"
        << " XXXXXXX       XXXXXXX     OOOOOOOOO\n"
        << "    .ein einfaches Tic-Tac-Toe-Spiel\n\n";

    // Auswahl des Gegners
    cout << "Waehle Gegner. Mensch (1) oder Computer (2): ";
    cin >> opponentChoice;

    // Falls der Gegner ein Computer ist, Schwierigkeitsgrad auswählen
    if (opponentChoice == 2) {
        cout << "Waehle Schwierigkeitsgrad. Einfach (1) oder Schwer (2): ";
        cin >> difficultyChoice;

        // Waehl das Symbol des Spielers
        cout << "Waehle dein Symbol (X oder O): ";
        char choice;
        cin >> choice;
        currentPlayer = (choice == 'X' || choice == 'x') ? 'X' : 'O';
        opponentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
    }
    else {
        // Mensch gegen Mensch: Spieler 1 ist immer 'X', Spieler 2 ist immer 'O'
        currentPlayer = 'X';
        opponentPlayer = 'O';
    }

    // Initialisieren, ob es der erste Zug des Computers ist
    bool isFirstMove = (currentPlayer == 'O' && opponentChoice == 2 && difficultyChoice == 2);

    if (opponentChoice == 1) {
        // Mensch gegen Mensch
        bool playerTurn = true;
        while (!isBoardFull(board)) {
            printBoard(board);
            if (playerTurn)
                playerMove(board, currentPlayer);
            else
                playerMove(board, opponentPlayer);

            if (checkWin(board, currentPlayer)) {
                printBoard(board);
                cout << endl << "Spieler " << currentPlayer << " hat gewonnen!" << endl;
                return 0;
            }
            if (checkWin(board, opponentPlayer)) {
                printBoard(board);
                cout << endl << "Spieler " << opponentPlayer << " hat gewonnen!" << endl;
                return 0;
            }
            playerTurn = !playerTurn;
        }
        printBoard(board);
        cout << endl << "Das Spiel endet Unentschieden!" << endl;
    }
    else if (opponentChoice == 2) {
        // Mensch gegen Computer
        bool playerTurn = (currentPlayer == 'X'); // Wenn Spieler X ist, beginnt er
        if (currentPlayer == 'O') {
            computerMove(board, opponentPlayer, currentPlayer, difficultyChoice == 2, isFirstMove);
            isFirstMove = false; // Nach dem ersten Zug wird der Flagg auf false gesetzt
            playerTurn = true;
        }

        while (!isBoardFull(board)) {
            printBoard(board);
            if (playerTurn) {
                playerMove(board, currentPlayer);
            }
            else {
                computerMove(board, opponentPlayer, currentPlayer, difficultyChoice == 2, isFirstMove);
                isFirstMove = false; // Nach dem ersten Zug wird der Flagg auf false gesetzt
            }

            if (checkWin(board, currentPlayer)) {
                printBoard(board);
                cout << endl << "Spieler " << currentPlayer << " hat gewonnen!" << endl;
                system("pause");
                return 0;
            }
            if (checkWin(board, opponentPlayer)) {
                printBoard(board);
                cout << endl << "Computer " << opponentPlayer << " hat gewonnen!" << endl;
                system("pause");
                return 0;
            }
            playerTurn = !playerTurn;
        }
        printBoard(board);
        cout << endl << "Das Spiel endet Unentschieden!" << endl;
    }
    else {
        cout << endl << "Ungueltige Auswahl. Das Spiel ist beendet." << endl;
    }

    system("pause");
    return 0;
}
