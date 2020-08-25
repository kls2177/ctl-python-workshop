# NumPy / Matplotlib

## Last Session

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
* To declare an array
    * `a = [1,2,3]`
* To declare a dictionary
    * `d = {"name": "Student"}`

## NumPy
NumPy is a Python package that provides more functionalities to vanilla Python.
It is mainly used for scientific computing.

Imagine you want to multiply `[1,3,4]` and `[5,6,7]` element by element.

a = [1, 2, 3]
b = [4, 5, 6]
result = []
for i in range(3):
    result.append(a[i] * b[i])
print(result)

It is much easier to use NumPy.

import numpy as np
result = np.array([1,2,3]) * np.array([4,5,6])
print(result)

To use NumPy, we first need to import it.

import numpy as np
np.__version__

> *Side note:* You can check the numpy version using `np.__version__`:

### NDArray
The most fundamental datastructure within NumPy is called NDArray.

You can create a NDArray by simply converting regular Python lists.

a = np.array([9,7,0,1])
print(a)

#### Data Types

Type defines what type of data is contained within an array.
> *All elements within a NDArray must be the same type, unlike Python lists.*

> **Common data types within NumPy**
  * `int32` - 32-bit integer, -2147483648 to 2147483647
  * `int64` - 64-bit integer, -9223372036854775808 to 9223372036854775807
  * `float32` - Single precision float
  * `float64` - Double precision float
  * `complex64` - Complex number represented by 2 32-bit floats
  * `complex128` - Complex number represented by 2 64-bit floats

To see what type of data is contained with in an array, use the following command.

a.dtype

#### Shape

Shape defines how many elements an array can contain within each dimension.

To see the shape of an array, use the following command.

a.shape # 1 dim array with 4 elements

b = np.array([[9,7,0,1], [6,3,2,0]])
b.shape # 2 x 4 array

> In general, a n-dimension array has the shape of

> `shape = (xn, xn-1, xn-2, …, x1)`

> $n$ is the dimension count. $x_i$ is the element count at $i^{th}$ dimension.

#### Array Creation

Not just converting lists to arrays, NumPy also provides many helpful functions to let you quickly create them from scratch.

zeros = np.zeros((3,3)) # 3x3 array filled with zeros
print(zeros)

ones = np.ones((4,5)) # 4x5 array filled with ones
print(ones)

r = np.arange(5, 9) # 5 to 8
print(r)

e = np.full((2,7,3), np.e) # 2x7x3 array filled with e
print(e)

c_zeros = np.zeros((2,2), dtype=np.complex64) # 2x2 array with complex zeros
print(c_zeros)

lin = np.linspace(0, 20, 10, dtype=np.int) # Linearly spaced array
print(lin)

log = np.logspace(0, 20, 10) # Log spaced array
print(log)

> **Most used array creation functions**
  * `np.empty(shape[, dtype, order])` - Create an empty array with no values.
  * `np.ones(shape[, dtype, order])` - Create an array with 1s.
  * `np.zeros(shape[, dtype, order])` - Create an array with 0s.
  * `np.full(shape, fill_value[, dtype, order])` - Create an array with `fill_value`s.
  
> Following are very similar to above functions, but instead of passing `shape`, you pass another array, and it will create a new array with the same shape.
  * `np.empty_like(a[, dtype, order, subok])`
  * `np.ones_like(a[, dtype, order, subok])`
  * `np.zeros_like(a[, dtype, order, subok])`
  * `full_like(a, fill_value[, dtype, order, subok])`

> Creating ranges
  * `np.arange([start,] stop[, step,][, dtype])` - Evenly spaced values
  * `np.linspace(start, stop[, num, endpoint, ...])` - Evenly spaced values, however you can specify `start`
  * `np.logspace(start, stop[, num, endpoint, base, ...])` - Spaced evenly on log scale
  * `np.geomspace(start, stop[, num, endpoint, dtype])` - Spaced evenly on log scale (geometric progression)

#### Indexing
Index for NumPy arrays is very similar to Python lists.

b[1][2]

# You can also use this syntax
b[1,2]

#### Array Operations

# First define two arrays
k = np.array([1.0, 2.0, 3.0])
j = np.array([2.0, 2.0, 2.0])

You can do basic arithmetic operations on two arrays.

c = k + j
print(c)

c = k * j
print(c)

Notice the result of `k * j` might be weird if you are familiar with matrices.

**Array != Matrix**

Array operations are element-wise, which means `k * j` simply multiplies the elements with same index. Most cases, you would operate on two arrays with the same shape. You can, however, operate on two different shaped arrays, this brings us to **broadcasting**.

#### Broadcasting
Broadcasting allows array operations to occur within C instead of Python. Which is much faster.

And it allows us to operate on differently shaped arrays, with some constraints.

![](https://www.evernote.com/l/Aq2wONNsbSFJ_Z7_JyPS3U5T3QQ3ULrYrVgB/image.png)

![](https://www.evernote.com/l/Aq3NWqDzrodAxJe2An6QGBOmGDDWtJFA-5MB/image.png)

![](https://www.evernote.com/l/Aq18pMOG1uxFEbV_6c6dJ5Ie3RIu5-JkEuoB/image.png)

![](https://www.evernote.com/l/Aq1F-XUu2GtKVLD1aBhxoDniSfD43QHbyooB/image.png)

> If you wish to learn more, follow this link: http://scipy.github.io/old-wiki/pages/EricsBroadcastingDoc

## Break
https://goo.gl/forms/m4vcs0RtPAVZawX93

## Matplotlib
Matplotlib is a very popular plotting library for Python. https://matplotlib.org.


# Import matplotlib
from matplotlib import pyplot as plt

Let's start by plotting some arrays with colour mesh!
Colour mesh can plot simple 2-d arrays.

a = np.ones((1,1000))
b = np.linspace(-20, 20, 1000)
print(a.shape, b.shape)
mesh = a * b
print(mesh.shape)

plt.pcolormesh(mesh)
plt.colorbar()

# Use meshgrid (https://docs.scipy.org/doc/numpy/reference/generated/numpy.meshgrid.html)
mesh_b = np.ones((1,1000)) * np.linspace(-20, 20, 1000)
print(mesh_b.shape)
xx, yy = np.meshgrid(mesh, mesh_b)
print(xx.shape,yy.shape)
mesh_c = xx * yy
print(mesh_c.shape)

plt.pcolormesh(mesh_c)
plt.colorbar()

# Plot the transpose
plt.pcolormesh(mesh.T)

> There are many more operations you can do to arrays. Most of them are very intuitive, you don't even need a reference :).
  * `np.meshgrid(ndarray, ndarray)`
  * `np.reshape(ndarray, shape)`
  * `np.resize(ndarray, size)`
  * `np.tile(ndarray, reps)`
  * `ndarray.sum()`
  * `ndarray.mean()`
  * `ndarray.std()`
  * `plt.plot(x, y)`

> You can find the full NumPy reference here: https://docs.scipy.org/doc/numpy-1.13.0/reference/index.html

Now let's plot some graphs. To plot a graph, you will need x coordinates and y coordinates.

# Create our x coordinates
x = np.linspace(-np.pi, np.pi, 100)
# Our y will simply be sin(x)
y = np.sin(x)

We now have x and y coordinates, we can plot the graph.

plt.plot(x, y)

You can play around with the styling, and generate more interesting graphs.

plt.plot(x, y, 'o')

plt.plot(x, y, 'go')

plt.plot(x, y, 'r+')

> Format string
  * Format string is with the format of `fmt = '[color][marker][line]'`
  * For example, `r+` simply means red with + marker.
  * Full documentation can be found at: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot under Notes secion.

You can plot multiple sets of data on the same graph.

plt.plot(x, y, 'r+')
plt.plot(x, np.cos(x), 'go', linewidth=4)

It might be very hard to make out what above graph is, we can use legends to solve this.

There are more fancy stuff you can do with graphs you will see later.

plt.plot(x, y, 'r+', label="sine")
plt.plot(x, np.cos(x), 'go', linewidth=4, label="cosine")
plt.legend(loc="upper left")

## Real Data

Now let's plot some real data.

You should already have the `argo_float_4901412.npz` file under this folder, if not, download it from https://www.ldeo.columbia.edu/~rpa/argo_float_4901412.npz.

Before plotting, let's load the file into NumPy.

data = np.load('argo_float_4901412.npz')

We can examine the data using some simple commands.

data.files

S is for salinity, T is for temperature and P is for density.

data['levels']

data['T'].shape

data['levels'].shape

You can also do regular NumPy operations on `data`.

data['levels'].min()

Data is collected bi-monthly.

data['date']

data['T'].min()

Oops! NumPy just encountered an error. This means there are invalid entries within column T.

If we examine the `T` column, you should see some entries are `nan`.

data['T']

We cannot proceed until this issue is resolved. We have a few options:
* Delete `nan` entries? You can’t delete the invalid entry, that will mess up the shape.
* Manually assign fake values? It can be tedious.

Usually if this happends, we use something called **Masked Arrays**.

T = np.ma.masked_invalid(data['T'])
print(T)

Above command will create a new masked array called `T` with all invalid entries masked.

A mask is simply an array with same shape as data, with 0 and 1 as values. If value is 1, then corresponding data will be ignored.

mx = np.array([1,2,3,np.float('nan'),5])
print(mx)
print(mx.mean())

mx = np.ma.masked_array(np.array([1,2,3,4,5]), mask=[0, 0, 0, 1, 0])
print(mx)
print(mx.mean())

We can now fix our data!

T = np.ma.masked_invalid(data['T'])
S = np.ma.masked_invalid(data['S'])
P = np.ma.masked_invalid(data['P'])

Now the data is fixed, we can plot it.

First, let's do a histogram of T

plt.hist(np.ravel(T).compressed()) #compressed ignores the masked values

plt.figure(figsize=(15,5))

plt.subplot(1,2,1)
plt.plot(T[0,:],label = 'Surface')
plt.plot(T[60,:],label = str(np.round(np.mean(P[60,:]))) + ' db')
plt.legend(loc = 'upper left')

plt.subplot(1,2,2)
plt.plot(S[0,:])
plt.plot(S[60,:])

Now, let's do a scatter plot. A T-S plot is a common way to plot ocean properties.

plt.scatter(S, T, c=P)

#### More Plots

Play around with matplotlib! It is more powerful than you think.

# Plot with title
plt.scatter(S, T, c=P)
plt.title("My Plot Title")
plt.show()

# Plot with x and y labels
plt.scatter(S, T, c=P)
plt.title("My Plot Title")
plt.xlabel("My X")
plt.ylabel("My Y")
plt.show()

# Resize plot
plt.figure(figsize=(20,10)) # Resize
plt.scatter(S, T, c=P)
plt.title("My Plot Title")
plt.xlabel("My X")
plt.ylabel("My Y")
plt.show()

# Plot with color bar
plt.figure(figsize=(10,5))
plt.scatter(S, T, c=P)
plt.title("My Plot Title")
plt.xlabel("My X")
plt.ylabel("My Y")
plt.colorbar() # Add color bar
plt.show()

# Multiple plots

plt.figure(figsize=(15,5))

plt.subplot(1,2,1)

plt.scatter(S, T, c=P)
plt.title("My Plot Title")
plt.xlabel("My X")
plt.ylabel("My Y")
plt.colorbar() # Add color bar

plt.subplot(1,2,2)
plt.plot(x, y)

plt.show()

# Plot with different colour

plt.figure(figsize=(15,5))

plt.subplot(1,2,1)

plt.scatter(S, T, c=P)
plt.title("My Plot Title")
plt.xlabel("My X")
plt.ylabel("My Y")
plt.colorbar()

plt.subplot(1,2,2, facecolor='y')
plt.plot(x, y, 'wo-')

plt.show()

# Plot with math text on it

plt.figure(figsize=(15,5))

plt.subplot(1,2,1)

plt.scatter(S, T, c=P)
plt.title("My Plot Title")
plt.xlabel("My X")
plt.ylabel("My Y")
plt.colorbar()

plt.subplot(1,2,2, facecolor='y')
plt.plot(x, y, 'wo-')
plt.text(0, -0.6, r'$sin(x)$', fontsize=20)

plt.show()

## Plotting Resources

https://matplotlib.org/gallery.html
Great place to find more demos.

Let's suppose we want to compute the density of our samples using an equation of state for sea water.

$\rho$ = $\rho_{0}$ + AS + BS$^{1.5}$ + CS$^{2}$

where A and B are functions for temperature.

rho_0 = 999.842594 + 6.793952e-2*T - 9.095290e-3*T**2 + 1.001685e-4*T**3 - 1.120083e-6*T**4 + 6.536332e-9*T**5
A = 8.24493e-1 - 4.0899e-3*T + 7.6438e-5*T**2 - 8.2467e-7*T**3 + 5.3875e-9*T**4
B = 5.72466e-3 + 1.0227e-4*T - 1.6546e-6*T**2
C = 4.8314e-4

rho = rho_0 + A*S + B*S**(1.5) + C*S**2

plt.figure(figsize=(15,5))

plt.subplot(1,2,1)

plt.scatter(rho, T, c=P)
plt.title("My Plot Title")
plt.xlabel("My X")
plt.ylabel("My Y")
plt.colorbar()

plt.subplot(1,2,2)
plt.scatter(rho, S, c=P)
plt.title("My Plot Title")
plt.xlabel("My X")
plt.ylabel("My Y")
plt.colorbar()

plt.show()

P[70]

