'''
Write a Python program to perform following operation on given string input:
a) Count Number of Vowel in given string
b) Count Length of string (do not use Len ())
c) Reverse string
d) Find and replace operation
e) check whether string entered is a palindrome or not

'''

# a) Count Number of Vowel in given string

string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in string:
    if char in vowels:
        count += 1
        # print(char)

print(f"The number of vowels in the string is: {count}")


# b) Count Length of string (do not use Len ())

print(f"The length of the string is: {len(string)}")


# c) Reverse string

print(f"The reversed string is: {string[::-1]}")


# d) Find and replace operation

string = input("Enter a string: ")

old_word = input("Enter the word you want to replace: ")

new_word = input("Enter the word you want to replace with: ")

print(string.replace(old_word, new_word))


# e) check whether string entered is a palindrome or not

string = input("Enter a string: ")

if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    

