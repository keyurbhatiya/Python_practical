# Write a Python program to check if the number provided by the user is a palindrome or not.


def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

num = int(input("Enter a number: "))

if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

