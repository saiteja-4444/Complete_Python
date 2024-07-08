# write a program for table creation using for loop.

for i in range(1,11):
    for j in range(11):
        print(i,'*',j,'=',i*j)
    print()


# Write a program for table creation using while loop.

 n=int(input("How many tables:"))
a=1
while a<=n:
    b=1
    while b<=10:
        print(a,'*',b,'=',a*b)
        b+=1
    print()
    a+=1


# single table creation using while loop

a=int(input("enter your table:"))
b=1
while b<=10:
    print(a,'*',b,'=',a*b)
    b+=1


# single tgable creatio using for loop
n=int(input("Enter your table:"))
for i in range(n,n+1):
    for j in range(11):
        print(i,'*',j,'=',i*j) 
