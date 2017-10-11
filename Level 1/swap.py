# swapping 2 numbers

'''
this program takes 2 numbers from the user
and swaps them using a temp variable
at last prints both of them
'''

a = float(input("First number: "))
b = float(input("Second number: "))

temp = a
a = b
b = temp

print("First number: ", a)
print("Second number: ", b)

'''
this program is also possible without using a temp variable
code of which, will be available in this same directory
'''
