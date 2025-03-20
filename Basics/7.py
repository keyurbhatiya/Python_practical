# Write a Python program to check if the number provided by the user is an Armstrong number.


def is_armstrong_number(num):
    num_str = str(num)
    num_length = len(num_str)
    sum = 0

    for i in range(num_length):
        digit = int(num_str[i])
        sum += digit ** num_length

    if sum == num:
        return True
    else:
        return False    

num = int(input("Enter a number: "))

if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")