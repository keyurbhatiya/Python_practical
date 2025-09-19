# Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal

decimal = int(input("Enter a decimal number: "))

binary = bin(decimal) #
octal = oct(decimal)
hexadecimal = hex(decimal)

print(f"Binary: {binary[2:]}") 
print(f"Octal: {octal[2:]}")
print(f"Hexadecimal: {hexadecimal[2:]}")
