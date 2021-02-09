#!/usr/bin/env python
# coding: utf-8

# # Part II: Matplotlib
# 
# ## 3. Matplotlib
# [Matplotlib](https://matplotlib.org) is the most popular plotting library for Python. 
# 
# We will take a look at several examples below, but the Matplotlib [gallery](https://matplotlib.org/gallery/index.html) is a great place to search for snippets of code to make your plots look professional.
# 

# ### 3.1 Importing Matplotlib
# 
# To use Matplotlib, we first need to import it. Matplotlib has many sub-packages, so we will import the pyplot sub-package.

# In[1]:


# Import matplotlib
from matplotlib import pyplot as plt

# Import numpy again too
import numpy as np


# Now let's plot some graphs. To plot a graph, you will need x coordinates and y coordinates. 
# 
# Let's plot a sine wave. We can use NumPy to do all sorts of [mathematical operations](https://numpy.org/doc/stable/reference/routines.math.html), like computing the sine of a variable.

# In[2]:


# Create our x coordinates (note the np.sine() function takes radians as an input)
x = np.linspace(-2*np.pi, 2*np.pi, 200)

# Our y will simply be sin(x)
y = np.sin(x)


# We now have our x and y coordinates - we can plot the graph. What do you think it will look like?

# In[3]:


# Make a simple line plot
plt.plot(x, y)


# There is so much styling of plots that you can do and we will by no means cover everything, but we will take a look at a few of the available options. 
# 
# First, we can change the line to a series of points using *markers*

# In[4]:


# Make a simple plot using markers ('o')
plt.plot(x, y, 'o')


# The default plotting colour is blue, but you can change this. Below I have changed the colour - can you guess what colour will appear based on the code?

# In[5]:


# Make a simple plot using green markers
plt.plot(x, y, 'go')


# What will the next example look like?

# In[6]:


# Make a simple plot using red markers
plt.plot(x, y, 'r+')


# The syntax used above to style our plots uses a *format string*:
# 
# **Format string**
# 
# > Format string is with the format of fmt = '[color][marker][line]'
# For example, r+ simply means red with + marker.
# Full documentation can be found at: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot under Notes secion.
# You can plot multiple sets of data on the same graph.

# In[ ]:





# In[7]:


# Plot with two curves
plt.plot(x, y, 'r+')
plt.plot(x, np.cos(x), 'go', linewidth=4)


# If we have two or more curves in the same plot, as above, how can we convey to the reader which line is which? We can use legends. To use a legend in Matplotlib, you indicate the legend *label* in the plotting command and then invoke the legend function separately include the legend in the plot.

# In[8]:


# Plot with two curves and a legend
plt.plot(x, y, 'r+', label="sine")
plt.plot(x, np.cos(x), 'go', linewidth=4, label="cosine")
plt.legend(loc="lower left")


# Finally, no plot is complete without a title and labels on the axes. Let's take a look at how to add these.

# In[9]:


# Plot with two curves, a legend and labels
plt.plot(x, y, 'r+', label="sine")
plt.plot(x, np.cos(x), 'go', linewidth=4, label="cosine")
plt.legend(loc="lower left")

# add labels
plt.title("Sine and Cosine Waves")
plt.ylabel("Amplitude")
plt.xlabel("Time")


# In[10]:


## REAL DATA!


# ### 1.3 Plotting 2-Dimensions
# Since NumPy is all about multi-dimensional data, we will now take a look at how to create 2-D plots. We will first make some plots using simple arrays and then we'll take a look at some real data.

# In[11]:


a = np.ones((1,1000))
b = np.linspace(-20, 20, 1000)
print(a.shape, b.shape)
mesh = a * b
print(mesh.shape)


# In[12]:


plt.pcolormesh(mesh)
plt.colorbar()


# In[13]:


# Use meshgrid (https://docs.scipy.org/doc/numpy/reference/generated/numpy.meshgrid.html)
mesh_b = np.ones((1,1000)) * np.linspace(-20, 20, 1000)
print(mesh_b.shape)
xx, yy = np.meshgrid(mesh, mesh_b)
print(xx.shape,yy.shape)
mesh_c = xx * yy
print(mesh_c.shape)


# In[14]:


plt.pcolormesh(mesh_c)
plt.colorbar()


# In[15]:


# Plot the transpose
plt.pcolormesh(mesh.T)


# > There are many more operations you can do to arrays. Most of them are very intuitive, you don't even need a reference :).
#   * `np.meshgrid(ndarray, ndarray)`
#   * `np.reshape(ndarray, shape)`
#   * `np.resize(ndarray, size)`
#   * `np.tile(ndarray, reps)`
#   * `ndarray.sum()`
#   * `ndarray.mean()`
#   * `ndarray.std()`
#   * `plt.plot(x, y)`
# 
# > You can find the full NumPy reference here: https://docs.scipy.org/doc/numpy-1.13.0/reference/index.html

# We will take a look at some other plotting options in the next exercise.
