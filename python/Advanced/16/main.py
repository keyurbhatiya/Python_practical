# main.py - Example program using the utils module

# Import the utils module
import utils

def main():
    # Test arithmetic functions
    print("Addition: 5 + 3 =", utils.add(5, 3))
    print("Subtraction: 10 - 4 =", utils.subtract(10, 4))
    print("Multiplication: 6 * 7 =", utils.multiply(6, 7))
    
    try:
        print("Division: 15 / 3 =", utils.divide(15, 3))
        print("Division: 10 / 0 =", utils.divide(10, 0))  # This will raise an error
    except ValueError as e:
        print("Error:", e)
    
    # Test greeting function
    print(utils.greet("Keyur"))

if __name__ == "__main__":
    main()