'''
Write a program which will allow user to enter 10 numbers and display largest oddnumber
from them. It will display appropriate message in case if no odd number is
found.

'''


def largest_odd_number():
    numbers = []
    
    print("Enter 10 numbers:")
    for i in range(10):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)
    
    odd_numbers = [num for num in numbers if num % 2 != 0]
    
    if odd_numbers:
        print(f"The largest odd number is: {max(odd_numbers)}")
    else:
        print("No odd numbers found!")

if __name__ == "__main__":
    largest_odd_number()
