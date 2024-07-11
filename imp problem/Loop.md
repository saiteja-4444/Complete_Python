# Table Creation using for Loop

``` python
for i in range(0,11):
    for j in range(0,11):
        print(i,'*',j,'=',i*j)
    print()
```

# Table creation using While Loop
``` python
a=1
while a<=10:
    b=1
    while b<=10:
        print(a,'*',b,'=',a*b)
        b+=1
    print()
    a+=1
```

# Single table creation using for loop
``` python
n=int(input("Enter your table:"))
for i in range(n,n+1):
    for j in range(0,11):
        print(i,'*',j,'=',i*j)
```

# Single table creation using while loop

``` python
a=int(input("enter your table:"))
b=1
while b<=10:
    print(a,'*',b,'=',a*b)
    b+=1
```


# Dynamic waty for table creation using while Loop

``` python
n=int(input("How many tables:"))
a=1
while a<=n:
    b=1
    while b<=10:
        print(a,'*',b,'=',a*b)
        b+=1
    print()
    a+=1
```
