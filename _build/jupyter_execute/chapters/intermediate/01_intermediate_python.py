# Part I: NumPy

## Review of Module 1

Take a few minutes to review the content of Module 1. Module 2 builds on what was covered in Module 1.

* To open a Python interpreter, type `python` in terminal.
* Arithmetic operations:
    * `+` Plus
    * `-` Minus
    * `*` Multiply
    * `/` Divide
    * `**` Power
    * `//` Divide and floor
    * `%` Mod
* Conditionals
    * `if(expression)`
    * `elif`
    * `else`
* Loops
    * `while(expression)`
    * `for`
* Some types are not compatible with each other.
    * `1+ "123"` is invalid.
* To declare a list
    * `a = [1,2,3]`
* To declare a dictionary
    * `d = {"name": "Student"}`

## 1. Why NumPy?

Let's take a look at the example in the video. 

Imagine you want to multiply two lists, `[1,3,4]` and `[5,6,7]`, element by element. We can do this by looping over the elements of each list, multiplying them and then storing them in a new list.

# multiplying two lists element-wise
a = [1, 2, 3]
b = [4, 5, 6]
result = []
for i in range(3):
    result.append(a[i] * b[i])
print(result)

This is pretty cumbersome. NumPy allows us to do these types of element-wise operations with ease.

# import NumPy
import numpy as np # we import it "as np" just so that we don't have to type "numpy" all the time.

result = np.array(a) * np.array(b)
print(result)

NumPy also allows us to store multi-dimensional data. For example, in climate science (my field), we are often working with data that has three spatial dimensions (latitude, longitude and height) as well as the time dimension.  

### 1.1. Importing NumPy

To use NumPy, we first need to import it. 

# import NumPy
import numpy as np

# what version are we using? 
np.__version__

> *Side note:* You can check the numpy version using `np.__version__`:

### 1.2 NDArray
The fundamental data structure within NumPy is called an NDArray (ND = *N*-dimensional).

One way to create a NDArray by converting a regular Python list.

a = np.array([9,7,0,1])
print(a)

#### 1.2.1 Data Types

`dtype` defines what type of data is contained within an array.
> *All elements within a NDArray must be the **same type**, unlike Python lists.*

> **Common data types within NumPy**
  * `int32` - 32-bit integer, -2147483648 to 2147483647
  * `int64` - 64-bit integer, -9223372036854775808 to 9223372036854775807
  * `float32` - Single precision float
  * `float64` - Double precision float
  * `complex64` - Complex number represented by 2 32-bit floats
  * `complex128` - Complex number represented by 2 64-bit floats

To see what type of data is contained with in an array, use the following command.

# data type in an array
a.dtype

#### 1.2.2 Shape

Shape defines how many elements an array can contain within each dimension.

To see the shape of an array, use the following command.

# 1 dimensional array with 4 elements
a.shape

So, we see that a has one dimension with 4 elements. Let's try buidling another array with multiple dimensions. What is the shape `b`?

# dimensional array
b = np.array([[9,7,0,1], [6,3,2,0]])
print(b.shape)

In general, an $N$-dimensional array has the shape of

> `shape = (x_N, x_{N-1}, x_{N-2}, …, x_1)`

$N$ is the dimension count. $x_i$ is the element count at $i^{th}$ dimension.

So, in the case of the above array, we start from the outer `[]` and work our way in. Within the first set of `[]`, we have 2 lists, so the number of elements in the Nth dimension is 2. Within the next set of `[]` we see that each list consists of 4 elements, so the number of elements in the N-1th dimension is 4. Thus, the shape is (2,4).

### 1.3 Array Creation

Above, we created an NDarray by converting lists to arrays using the `np.array()` function. But, NumPy also provides many helpful functions to let you quickly create arrays from scratch.

# 3x3 array filled with zeros
zeros = np.zeros((3,3)) 
print(zeros)

Creating an array of zeros is useful of initializing an array that you will then populate. 

You can also specify the data type. In the example below, we are creating an array of zeros, but we want the data type to be complex.

c_zeros = np.zeros((2,2), dtype=np.complex64) # 2x2 array with complex zeros
print(c_zeros)

We can also create an array of ones. This is useful if we need an array of a particular constant. You can simply multiply the entire array by the constant of interest. 

# 4x5 array filled with ones
ones = np.ones((4,5)) 
print(ones)

# 4x5 array filled with twos
twos = 2 * np.ones((4,5)) 
print(twos)

An alternative way to fill an array with a constant is to use `np.full()`.

# 2x7x3 array filled with e
e = np.full((2,7,3), np.e)
print(e)

You can also use the [`np.arange()`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html) function to create a 1-D array of consecutive numbers. `np.arange()` is similar to the `range()` function we discussed in Module 1.

In the example below, what will the array look like?

# array using np.arange
r = np.arange(5, 9)
print(r)

`np.linspace()` is similar to `np.arange()` except that the `stop` value is included and rather than specify the `step` you specify the number of elements you want. These elements will be linearly spaced.

So, in the example below, what value will the array start with? Stop with? How many values will there be?

# Linearly spaced array
lin = np.linspace(0, 18, 10, dtype=np.float)
print(lin)

Now, change the above so that the `stop` value is 19. What happens? Keep `stop` at 19 and change the number of elements to 20. What happens?

`np.logspace()` is similar to `np.linspace()` except that the number will be spaced logarithmically.

# Log spaced array
log = np.logspace(0, 18, 10, base = 10) 
print(log)

# Log spaced array
log = np.logspace(0, 18, 10, base = np.e) 
print(log)

Here is a summary of the most commonly used array creation functions.

#### **The most commonly used array creation functions**
>  * `np.empty(shape[, dtype, order])` - Create an empty array with no values.
>  * `np.ones(shape[, dtype, order])` - Create an array with 1s.
>  * `np.zeros(shape[, dtype, order])` - Create an array with 0s.
>  * `np.full(shape, fill_value[, dtype, order])` - Create an array with `fill_value`s.
  
The following are very similar to the above functions, but instead of passing `shape`, you pass another array, and it will create a new array with the same shape.
>  * `np.empty_like(a[, dtype, order, subok])`
>  * `np.ones_like(a[, dtype, order, subok])`
>  * `np.zeros_like(a[, dtype, order, subok])`
>  * `full_like(a, fill_value[, dtype, order, subok])`

The following functions are for creating ranges
>  * `np.arange([start,] stop[, step,][, dtype])` - Evenly spaced values
>  * `np.linspace(start, stop[, num, endpoint, ...])` - Evenly spaced values, however you can specify `start`
>  * `np.logspace(start, stop[, num, endpoint, base, ...])` - Spaced evenly on log scale
>  * `np.geomspace(start, stop[, num, endpoint, dtype])` - Spaced evenly on log scale (geometric progression)

### 1.4 Indexing
Indexing for NumPy arrays is very similar to Python lists, except that we have to index for more than one dimension.

Let's start with the array `b` that we defined above.

b = np.array([[9,7,0,1], [6,3,2,0]])
print(b)
print(b.shape)

Suppose we want to extract the element with the value "2". How do we do this? First, let's consider the shape of `b`. What element contains "2" within the 1st dimension (the dimension with 4 elements)? Remember that we count from zero in python. What element contains "2" within the 2nd dimension (the dimension with 2 elements)? 

If you guessed the 2nd and 1st elements, you are correct!

There are two ways to index arrays. The first is to use consecutive `[]` as shown below.

# indexing - method 1
b[1][2]

Or you can use the syntax below (this is the syntax that I normally use).

# indexing - method 2
b[1,2]

## 2. Array Operations

Being able to perform element-wise operations is what makes NumPy so powerful. Let's take a look by first defining two arrays.

# First define two arrays
k = np.array([1.0, 2.0, 3.0])
j = np.array([2.0, 2.0, 2.0])

NumPy allows for basic arithmetic operations such as addition and multiplication. What do you get if you add `k` and `j` element-wise?

c = k + j
print(c)

What do you get if you multiply `k` and `j` element-wise?

c = k * j
print(c)

Notice the result of `k * j` might be weird if you are familiar with matrices.

**Array != Matrix**

Array operations are element-wise, which means `k * j` simply multiplies the elements with the same index. In most cases, you would operate on two arrays with the same shape (`k` and `j` have the same shape). You can, however, operate on two different shaped arrays under certain conditions. This brings us to **broadcasting**.

### 2.1 Broadcasting
Broadcasting allows us to operate on differently shaped arrays, with some constraints. Broadcasting means that array operations occur within C instead of Python, which is much faster.

And it .

![](https://www.evernote.com/l/Aq2wONNsbSFJ_Z7_JyPS3U5T3QQ3ULrYrVgB/image.png)

![](https://www.evernote.com/l/Aq3NWqDzrodAxJe2An6QGBOmGDDWtJFA-5MB/image.png)

![](https://www.evernote.com/l/Aq18pMOG1uxFEbV_6c6dJ5Ie3RIu5-JkEuoB/image.png)

![](https://www.evernote.com/l/Aq1F-XUu2GtKVLD1aBhxoDniSfD43QHbyooB/image.png)

> If you wish to learn more, follow this link: http://scipy.github.io/old-wiki/pages/EricsBroadcastingDoc