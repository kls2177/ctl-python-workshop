# Exercises: Part I

Here are few questions to test your knowledge. Try the questions first without using python. Then, you can test whether or not you have the right answer by typing out the multiple choice options in your own jupyter notebook.

```{admonition} Question 1
:class: tip
What is the correct way to import NumPy?

* (a) import np from numpy
* (b) from numpy import np
* (c) import numpy as np
* (d) import numpy as numpy
```

import numpy as np

```{admonition} Question 2
:class: tip
What is the shape of the array below?

* (a) (2,3)
* (b) (3,2)
* (c) (3,2,1)
* (d) (1,2,3)
```

a = np.array([[[1,2,3],[3,4,5]]])
print(a.shape)

```{admonition} Question 3
:class: tip
Which of the following operations is illegal in NumPy (For all options below, assume: a.shape = (4,3), b.shape = (3,), c.shape = (2,4), d is a scalar.)?

* (a) b * d
* (b) a * b
* (c) b * c
* (d) a * d
* (e) a * c
```

# let's create some hypothetical arrays
a = np.array([[1,2,3],[2,3,4],[3,4,5],[4,5,6]])
print(a.shape)
b = np.array([1,2,3])
print(b.shape)
c = np.array([[3,4,5,6],[4,5,6,7]])
print(c.shape)
d = 10.0

# Now try to perform the above operations and see what happens

```{admonition} Question 4 
:class: tip 
For the below array, what values will I get if I slice the array as follows: c[1,2:5]?

(a) [2,3,4,5]
(b) [13,14,15]
(c) [3,4,5,6]
(d) [12,13,14,15]
(e) [12,13,14]
```

c = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]])
print(c)

# slice
print(c[1,2:5])

```{admonition} Question 5
:class: tip 
How we can change the shape of the Numpy array in python? Hint: you will need to google this one.

(a) np.shape()
(b) np.reshape()
(c) np.swapaxes()
(d) np.ravel()
(e) np.rollaxis()

*Take a look at the example below to see how to change the shape of an array.
``` 


# This is a bit of a trick question!
# Options (b) - (e) all allow you to change the shape of an array to a certain extent.
# np.reshape() has the most functionality. Let's take a look at an example. 
# The shapes that we can choose in np.reshape() have to give the right number of total elements

print(c.shape)

# We can change the shape of c as follows:
d = np.reshape(c,[20,])
print(d.shape)
print(d)

# or we can do the following
f = np.reshape(c,[4,5])
print(f.shape)
print(f)