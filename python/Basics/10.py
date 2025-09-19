'''
Define a procedure histogram () that takes a list of integers and prints a histogram to thescreen.
For example, histogram ([4, 9, 7]) should print the following:
****
*********
*******

'''

def histogram(list):
    for num in list:
        print("*" * num)

histogram([4, 9, 7])
