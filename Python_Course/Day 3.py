#                                       OPERATORS AND CONTROL STATEMENT

# what is operator ?
"""
Operations are speciall symbol or keyword used to perfrom operation on variable and values. 
"""
# Types of operators
"""
1.Arithmetic operator
2.Assignment operator
3.Logical operator
4.Relational operator 
5.Membership operator
6.Bitwise operator
7.Identify operator
"""

# Arithmetic operator

a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
print("Addition",a+b)
print("subtraction",a-b)
print("Multiplication",a*b)
print("Division",a/b)


# Assignment operator
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
a+=b  # a = a+b
print(a)



# Realational operator

a=5
b=2
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)
print(a<b)
print(a>b)


#logical operator
a=9.99
print(a<10 and a>9)
print(a<9 or a>10)
print(a!= 0)



# Membership operator
a=[13,566,342,625,62,262,721,989]
print(13 in a)
print(7 not in a)


# Identify operator

a=3
b=5
print(a is b)
print(a is not b)


