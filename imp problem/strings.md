# String Methods
``` python
lower ()
upper ()
endswith ()
startswith ()
find ()
format ()
strip ()
lstrip ()
rstrip ()
split ()
join ()
isalpha ()
isnumeric ()
isalnum ()
title ()
replace ()
```

``` python
# lower and upper
a="SAI TEJA"
b="sai teja"
i=a.lower()
j=b.upper()
print(i)
print(j)

# count
ravi="i am a good person in the world."
print(ravi.count("i"))

# endswith and startswith
a="udemy.com"
print(a.endswith("com"))
print(a.startswith("udemy"))

# find and index
a="jai sree ram"
print(a.find("z")) # if you are mention unknown from the string it will print negative.
print(a.index("z")) # if you are mention unknown from the string it will error. 

# format
a="sai"
print("hi {} tinava ra".format(a))

# strip,lstrip,rstrip
a="   hi hello tinava raa    "
print(a.strip())
print(a.rstrip())
print(a.lstrip())


# split and join
a="i am very lazy untill i enter into the game"
x=a.split()
print(x)

b=["i dont care once","i was started ignore you"]
y=",".join(b)
print(y)



# isalpha isnumeric isalnum
a="abc123"
print(a.isalnum())
print(a.isalpha())
print(a.isnumeric())

# title
book="a research on milk quality detection"
# it will print first letter of the word in upper case
print(book.title())



# replace 
data="i am good am are worst"
s=data.replace("am","he").replace("good","bad").replace("i","they").replace("are","in")
print(s)
```

# Dynamic way to replace the string
``` python
a="way there is a will they is a way"
b=a.split()
c=[]
for i in b:
    if i=="they":
        i="there"
        c.append(i)
    else:
        c.append(i)
    e="".join(c)
print(c)
print(type(e))
```
