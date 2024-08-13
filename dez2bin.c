#include <stdio.h>

// Function to convert decimal number to binary
void convertToBinary(int decimalNumber) {
    if (decimalNumber == 0) {
        printf("0");
        return;
    }
    
    // Find the highest bit position
    int highestBit = 1;
    while (highestBit <= decimalNumber) {
        highestBit <<= 1;
    }
    
    // Print binary representation from left to right
    highestBit >>= 1; // Adjust to the highest bit position that is set

    // Temporary buffer to hold the binary representation
    char binaryBuffer[32];
    int index = 0;

    // Collect binary representation in the buffer
    while (highestBit > 0) {
        if (decimalNumber & highestBit) {
            binaryBuffer[index++] = '1';
        } else {
            binaryBuffer[index++] = '0';
        }
        highestBit >>= 1;
    }
    binaryBuffer[index] = '\0'; // Null-terminate the string

    // Print binary representation with 4-bit grouping from right to left
    int len = index;
    for (int i = 0; i < len; i++) {
        printf("%c", binaryBuffer[i]);
        // Print a space every 4 bits from the right
        if ((len - i - 1) % 4 == 0 && (len - i - 1) > 0) {
            printf(" ");
        }
    }
}

int main() {
    int decimalNumber;

    printf("Enter a decimal number: ");
    scanf("%d", &decimalNumber);

    printf("Binary: ");
    convertToBinary(decimalNumber);
    printf("\n");

    // Wait for any key
    scanf("%d", &decimalNumber);

    return 0;
}
