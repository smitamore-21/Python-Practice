# Program 5: Swap Two Numbers
# Description:
# Swap the values of two variables without using a third variable.

# Take two numbers as input from the user
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print("Before swaping :")
print("a =", a)
print("b =", b)

# Swap the values using arithmetic operations
a = a + b
b = a - b
a = a - b

# another way swaping two var
# a , b = b , a 

# Display the swapped values
print("After swaping :")
print("a =", a)
print("b =", b)