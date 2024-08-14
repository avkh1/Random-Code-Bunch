// Some Random Calculator v1.1j
// Andrei Avkhimovich
// for fun \o/

import java.util.Scanner;

public class ExpressionEvaluator {

    public static void main(String[] args) {
        System.out.println(" ____  ____  _      _____   ____  ____  _      ____  ____  _     ");
        System.out.println("/ ___\\/  _ \\/ \\__/|/  __/  /  __\\/  _ \\/ \\  /|/  _ \\/  _ \\/ \\__/|");
        System.out.println("|    \\| / \\|| |\\/|||  \\    |  \\/|| / \\|| |\\ ||| | \\|| / \\|| |\\/||");
        System.out.println("\\___ || \\_/|| |  |||  /_   |    /| |-||| | \\||| |_/|| \\_/|| |  ||");
        System.out.println("\\____/\\____/\\_/  \\|\\____\\  \\_/\\_\\\\_/ \\|\\_/  \\|\\____/\\____/\\_/  \\|");
        System.out.println("   ____  ____  _     ____  _     _     ____  _____  ____  ____     ");
        System.out.println("  /   _\\/  _ \\/ \\   /   _\\/ \\ /\\/ \\   /  _ \\/__ __\\/  _ \\/  __\\    ");
        System.out.println("  |  /  | / \\|| |   |  /  | | ||| |   | / \\|  / \\  | / \\||  \\/|    ");
        System.out.println("  |  \\__| |-||| |_\\/|  \\__| \\_/|| |_\\/| |-||  | |  | \\_/||    /    ");
        System.out.println("  \\____/\\_/ \\|\\____/\\____/\\____/\\____/\\_/ \\|  \\_/  \\____/\\_/\\_\\    ");
        System.out.println("                                                   .version 1.1");
        System.out.println("Verfugbare Symbole: + - * / ^ ( )");
        System.out.println("Beispiel: 1 + 2 * (3 ^ 2) / 4");
        System.out.print("Geben Sie die Formel ein: ");

        Scanner scanner = new Scanner(System.in);
        String expr = scanner.nextLine();
        scanner.close();

        try {
            int[] pos = {0};
            double result = parseExpression(expr, pos);
            skipWhitespace(expr, pos);
            if (pos[0] < expr.length()) {
                System.err.println("Fehler: Nicht alle Zeichen der Formel wurden verarbeitet");
                System.exit(1);
            }
            System.out.println("\n\nErgebnis: " + result);
        } catch (Exception e) {
            System.err.println("Fehler: " + e.getMessage());
            System.exit(1);
        }
    }

    private static void skipWhitespace(String expr, int[] pos) {
        while (pos[0] < expr.length() && Character.isWhitespace(expr.charAt(pos[0]))) {
            pos[0]++;
        }
    }

    private static double parseNumber(String expr, int[] pos) {
        skipWhitespace(expr, pos);
        int start = pos[0];
        while (pos[0] < expr.length() && (Character.isDigit(expr.charAt(pos[0])) || expr.charAt(pos[0]) == '.')) {
            pos[0]++;
        }
        if (start == pos[0]) {
            throw new RuntimeException("Fehler: Ungültige Zahl");
        }
        try {
            return Double.parseDouble(expr.substring(start, pos[0]));
        } catch (NumberFormatException e) {
            throw new RuntimeException("Fehler beim Parsen der Zahl");
        }
    }

    private static double parseParentheses(String expr, int[] pos) {
        skipWhitespace(expr, pos);

        if (expr.charAt(pos[0]) == '(') {
            pos[0]++; // '(' überspringen
            double value = parseExpression(expr, pos);
            skipWhitespace(expr, pos);
            if (expr.charAt(pos[0]) != ')') {
                throw new RuntimeException("Fehlende schließende Klammer");
            }
            pos[0]++; // ')' überspringen
            return value;
        }
        return parseNumber(expr, pos); // Hier wird parseNumber anstelle von parseFactor aufgerufen
    }

    private static double parseFactor(String expr, int[] pos) {
        double value = parseParentheses(expr, pos);

        while (pos[0] < expr.length()) {
            skipWhitespace(expr, pos);
            char op = expr.charAt(pos[0]);

            if (op == '^') {
                pos[0]++;
                double exponent = parseParentheses(expr, pos);
                value = Math.pow(value, exponent);
            } else {
                break;
            }
        }

        return value;
    }

    private static double parseTerm(String expr, int[] pos) {
        double value = parseFactor(expr, pos);

        while (pos[0] < expr.length()) {
            skipWhitespace(expr, pos);
            char op = expr.charAt(pos[0]);

            if (op == '*' || op == '/') {
                pos[0]++;
                double nextValue = parseFactor(expr, pos);
                if (op == '*') {
                    value *= nextValue;
                } else if (op == '/') {
                    if (nextValue == 0) {
                        throw new RuntimeException("Fehler: Division durch Null");
                    }
                    value /= nextValue;
                }
            } else {
                break;
            }
        }

        return value;
    }

    private static double parseExpression(String expr, int[] pos) {
        double value = parseTerm(expr, pos);

        while (pos[0] < expr.length()) {
            skipWhitespace(expr, pos);
            char op = expr.charAt(pos[0]);

            if (op == '+' || op == '-') {
                pos[0]++;
                double nextValue = parseTerm(expr, pos);
                if (op == '+') {
                    value += nextValue;
                } else if (op == '-') {
                    value -= nextValue;
                }
            } else {
                break;
            }
        }

        return value;
    }
}
