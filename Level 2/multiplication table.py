'''
This program prints multiplication table
of number entered by user
'''

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, " x ", i, " = ", i * n)
