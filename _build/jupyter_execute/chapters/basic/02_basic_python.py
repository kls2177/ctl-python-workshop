# Module 1: Basic Python (Part II)

## 5. Loops

Loops are important in programming as they allow you to execute a block of code repeatedly. It is very common that you may need to use a piece of code over and over but you do not want to write the same line of code multiple times.

There are two types of loops:

* `while` loops
* `for` loops

### 5.1 While Loops
While loops in Python follow the following format:
```
while expression:
    command1
    command2
    ...
```
Commands will keep executing until `expression` become False equivalent. Again, note the syntax - the expression is followed by a colon and the commands are indented.

Take a loop at the while loop below. What do you think the output will be? 

# A simple while loop
i = 10
while i:
    print(i**i)
    i = i - 1

Note that `i -= 1` is a shortcut for `i = i - 1`.

### 5.2 For Loops
You can use for loops to loop through a `range`. Later you will see it can also loop through lists.
```
for value in range(int):
    command1
    command2
    ...
```
This will loop and set `value` from 0 until `int - 1`

for value in range(10):
    print(value % 2)

## 6. Lists
You can store anything in a list, to create a list, use the following command:
```python
l = [] # l is now an empty list
```
You can also pre-populate the list:
```python
l = [1, 2, "hello"]
```

l = []
print(l)
l = [1, 2, "hello"]
print(l)

### 6.1 List Operations
There are many list operations you could do, following are just some basic examples.

# Append
l = [1, 3.4, "test"]
l.append("hi")
print(l)

# Pop
l = [1, 3.4, "hi"]
print(l.pop())
print(l)

# Access a value by index. Computer counts from 0!
l = [1, 3.4, "123"]
print(l[1])

# Concatenate two lists
a = [1,2]
b = [3,4]
print(a + b)

### Extract Data From Lists
Practice! These can be very confusing.

# Elements after index (inclusive)
l = [1,2,3,4,5,6,7]
print(l[2:])

# Elements before index (exclusive)
l = [1,2,3,4,5,6,7]
print(l[:3])

# Negative index (access from end)
l = [1,2,3,4,5,6,7]
print(l[-1])

# Elements between two indexes
l = [1,2,3,4,5,6,7]
print(l[2:6])

### More List Operations
* list.sort()
* list.remove()
* list.clear()
* list.reverse()
* ...

### Loop Through a List
You can use a for loop to loop through a list.

l = [1,3,6,"hi"]
for element in l:
    print(element)

## Tuples
Tuples are like lists, but immutable. You will see what immutable means later.

t = (1,2,3)
print(t)

t = (1,2,3)
for element in t:
    print(element)

## Dictionaries
Instead of having an numeric index for each value, dictionaries allows you to map a custom key to each value.

You can use almost anything as a key, it is quite flexible.

d = {
    'name': "Jun",
    'age': 20,
    True: 'yes',
    4: 5,
    False: (7,8)
}
print(d)

### Dictionary Operations
Below are some basic dictionary operations you could use.

# Add value
d = {}
d['test'] = 123
print(d)

# Access value
d = {'test': 123}
print(d['test'])

## Loop Through Dictionaries
You can loop through dictionaries using a for loop.

**Dictionaries are unorderd.** Thus the output order cannot be gurenteed.

d = {
    'name': "Jun",
    'age': 20,
    True: 'yes',
    4: 5,
    False: (7,8)
}
for key in d:
    print(key, d[key])

## Functions
Functions allow you to break your program into pieces. They also enable the ability to reuse code.

You define functions using following syntax:
```
def function_name(input_1, input_2):
    command1
    command2
    â€¦
    return value
```

Once a function returns, it will immediately exit.

# Example #1
def hi(name):
    return "hi " + str(name)
print(hi("Jun"))

# Example #2, optional inputs
def hi(name="Jun"):
    return "hi " + str(name)
print(hi())

# Example #3, flexible number of inputs
def get_sum(*input):
    result = 0
    for num in input:
        result += num
    return result
print(get_sum(1,2,3,-1,90))

## Mutable & Immutable Types
* Mutable
    * List, Dictionary
* Immutable
    * Integer, Float, String, Boolean, Tuple

# What will happen?
def weird_function(l):
    l[0] = 'interesting'
l = [1,2,3]
weird_function(l)
print(l)

As you can see, the function "mutated" the original list. However, if we change the list to a tuple...

```{figure} tuple.png
---
height: 150px
name: tuple
---
```

The function won't be able to mutate it anymore.

