def bintodec(binary_number):
    decimal_number = 0
    for digit in binary_number:
        decimal_number = decimal_number * 2 + int(digit)
    return decimal_number