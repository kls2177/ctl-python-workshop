# Introduction to Python

Let's start with a simple hello world program!

# Type your code below
print("Hello World!")

## Operations
Not just simple outputs, Python can also do **operations**.
* `+` Addition
* `-` Subtraction
* `*` Multiplication
* `/` Division
* `%` Modulus
* `**` Exponent

# Type your code below
1+2

# Type your code below
1.6*7.8

However, this is not really useful for complex computations. We need to store the result somehow.

Introducing **variables**.

## Variables

# Type your code below
a = 1.6*7.8
c = a+20
c

Order of operations matter! Try executing `5 + 4 * 16`

# Type your code below
5 + 4 * 16

## Order of Operations
* `()` Parentheses - Highest Precedence
* `**` Exponentiation
* `*` Multiplication
* `/` Division
* `%` Modulo
* `+` Addition
* `-` Subtraction

## Basic Data Types
* Integer (1,91,-1923)
* Float (1.1, -109.1, 1.00)
* String (â€œnameâ€, â€œhelloâ€, â€œ123â€)
* Boolean (True, False)

## Type Conversions
What if I want to add 1 and "2"?

```{figure} typeerror.png
---
height: 150px
name: typeerror
---
```

It will result in a `TypeError`. Some types are incompatible with each other, in this case you need to do type conversion.

# Type your code below
1 + int("2")

To check a value's type, use `type()` function.

# Type your code below
type(1)

## Conditionals
Conditionals in Python follow the follwing format:
```
if expression1:
    command1
elif expression2:
    command2
else:
    command3
```
* `command1` will execute if `expression1` is True equivalent.
* `command2` will execute if `expression1` is False equivalent, and `expression2` is True equivalent.
* Otherwise `command3` will execute.

# Type your code here
have_homework = True
if have_homework:
    print("Time to study!")
else:
    print("Time to play!")

### Comparators
Comparators will always resolve to a boolean value.

* `>` Greater than
* `<` Less than
* `>=` Greater or equal to
* `<=` Less or equal to
* `==` Equal
* `!=` Not equal

**IMPORTANT**: Equal comparator is double equal sign, not single.

### Logical Operators
You can use logical operators to connect multiple expressions.
* and
* or
* not

# Type your code here
have_homework = False
hours_studied = 10
if hours_studied > 4 and not have_homework:
    print("Time to play")

### True / False Equivalent
Expression does not have to be strictly `True` or `False` for Python conditionals to trigger.

* True
    * Boolean: True
    * Integer: not 0
    * String: not empty
    
* False
    * Boolean: False
    * Integer: 0
    * String: `""`

# Type your code here
a = 10
b = 20
c = 30
if a == 10:
    print("a is 10")
    
if b < a:
    print("b is less than a")
elif c and b and a:
    print("c,b,a are all True equivalents")
else:
    print("nothing happens")

You can also have nested blocks

# Type your code here
a = 10
b = 20
c = 30
if a == 10:
    print("a is 10")
    
if b < a:
    print("b is less than a")
elif c and b and a:
    print("c,b,a are all True equivalents")
    if c < 40:
        print("c is also smaller than 40")
else:
    print("nothing happens")

## Break

And a little quiz :)

https://goo.gl/forms/VoeETFMRQKWCNVYs1

## While Loops
While loops in Python follow the following format:
```
while expression:
    command1
    command2
    ...
```
Commands will keep executing until `expression` become False equivalent.

i = 10
while i:
    print(i**i)
    i -= 1

`i -= 1` is just a shortcut for `i = i - 1`.

## For Loops
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

## Lists
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

### List Operations
There are many list operations you could do, following are just some basic examples

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

## Exercises

Write a function that takes in a list, and returns the largest number. You cannot use built-in max().

You can assume input have at least 1 number.

def get_max(nums):
    current_max = nums[0]
    for num in nums:
        if num > current_max:
            current_max = num
    return current_max

get_max([-1,99,10,100,-91])

Write a function that takes in a list, returns a new reversed list. You **cannot** mutate the original list.

`help(list)` might be useful.

def get_reversed(l):
    new_l = l.copy()
    new_l.reverse()
    return new_l

l = [1,2,3]
print(get_reversed(l))
print(l)