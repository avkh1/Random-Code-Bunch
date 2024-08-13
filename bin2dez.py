# CONVERTS BIN TO DEZ
# Weeeeeee \o/
# Andi Avkh 01082024

def binary_to_decimal(binary_str):
    # Initialize the decimal number to 0
    decimal_number = 0
    
    # Iterate over each character in the binary string
    for digit in binary_str:
        # Shift the current decimal number to the left by 1 (equivalent to multiplying by 2)
        decimal_number = decimal_number * 2
        
        # Add the current binary digit (0 or 1) to the decimal number
        decimal_number += int(digit)
    
    return decimal_number


def binary_to_hex(binary_str):
    # Convert binary string to decimal using int function with base 2
    decimal_number = int(binary_str, 2)
    # Convert decimal number to hexadecimal using hex function and remove the '0x' prefix
    hex_number = hex(decimal_number)[2:]

    return hex_number.upper()



# MAIN PROC
binary_str = input("Enter some BIN number plz...: ")

decimal_number = binary_to_decimal(binary_str)
hex_number = binary_to_hex(binary_str)
print(f"The DEC representation of the binary is {decimal_number}")
print(f"The HEX representation of the binary is {hex_number}")

input()