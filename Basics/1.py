# Write a Python Program to Convert Celsius to Fahrenheit and vice –a-versa.


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C = {celsius_to_fahrenheit(celsius):.2f}°F")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit):.2f}°C")
    else:
        print("Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()
