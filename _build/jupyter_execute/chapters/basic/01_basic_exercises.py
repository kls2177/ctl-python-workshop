## Exercises: Part I

Here are few questions to test your knowledge. Try the questions first without using python. Then, you can test whether or not you have the right answer by typing out the multiple choice options in your own jupyter notebook.

```{admonition} Question 1
:class: tip
How do you print "hi" to screen in Python 3?

* (a) print(hi)
* (b) print "hi"
* (c) print("hi")
* (d) print hi
```

print("hi")

```{admonition} Question 2
:class: tip
Which one of the following expression will result in a "division by zero" error?

* (a) 61 / ((-8 + 2) * 4) ** 2
* (b) 61 // ((-8 + 2) * 4) ** 2
* (c) 61 // (-8 + 2 * 4) ** 2
* (d) 61 // ((-8 + 2) * 4) * 2
```

```{admonition} Question 3
:class: tip
What is the correct way to print "my age is " + age? Assume age is an integer.

* (a) print("my age is", age)
* (b) print("my age is" + age)
* (c) print("my age is" + str(age))
* (d) print("my age is" + age.toString())
```

age = 40
print("my age is " + str(age))

```{admonition} Question 4
:class: tip
Is following expression True or False? Hint: break the question down into smaller parts.

`("False" and True) or (False or 0 or -1)`

* (a) True
* (b) False
```

("False" and True) or (False or 0 or -1)

```{admonition} Question 5 
:class: tip 
What is the value of x after the execution of the code below completes?

* (a) 5
* (b) 4
* (c) 3
* (d) 2
```

x = 0
a = 0
b = -5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)

```{admonition} Question 6 
:class: tip 
What is the value of x after the execution of the code below completes?

* (a) 5
* (b) 4
* (c) 3
* (d) 2
```

x = 0
a = 5
b = 5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)

