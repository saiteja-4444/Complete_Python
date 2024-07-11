# Lists Methods
``` python
# append
append ()
extend ()
copy ()
clear ()
count ()
index ()
pop ()
remove ()
insert ()
sort ()
reverse ()
```


``` python
sai=[2,3,45]
sai.append("python")
print(sai)

# extend
sai=[23,34,52]
sai.extend(['python',12,34,'okay'])
print(sai)

# copy
sai=[23,34,52]
t=sai.copy()
sai.append("nooo")
print(sai,t)

# clear
sai=[23,34,52]
sai.clear()
print(sai)

# count
sai=[23,34,52,21,23,21,667,8,32,21]
print(sai.count(21))

# index
sai=[23,34,52,21,23,21,667,8,32,21]
print(sai.index(667))

# pop 
sai=[23,34,52,21,23,21,667,8,32,21]
sai.pop(5)
print(sai)


# remove
sai=[23,34,52,21,23,21,667,8,32,21]
sai.remove(21)
print(sai)


# insert
sai=[23,34,52,21,23,21,667,8,32,21]
sai.insert(1,'hello')
print(sai)


# sort 
sai=[23,34,52,21,23,21,667,8,32,21]
sai.sort()
print(sai)

# reverse
sai=[23,34,52,21,23,21,667,8,32,21]
sai.reverse()
print(sai)

```
