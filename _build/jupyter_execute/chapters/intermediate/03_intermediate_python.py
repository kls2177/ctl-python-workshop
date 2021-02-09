#!/usr/bin/env python
# coding: utf-8

# # Part III: Working with *Real Data*

# We have learned a lot about programming in python - the syntax and the functionality - but, for the most part, we have been using fairly simple examples and data sets. So, let's now take a look at how we might use python to work with some real data.
# 
# Download the following [file](https://github.com/kls2177/ccia_files/blob/master/argo_float_4901412.npz?raw=true) and save it in the same directory that you are working in. The data we will be working with is ocean temperature, salinity, and pressure from an [Argo float](https://argo.ucsd.edu/).
# 
# Argo floats are amazing! They are autonomous floats that drift and dive throughout the ocean (see [Figure](argo)) relaying information about temperature and salinity to satellites. 
# 
# ```{figure} argo.png
# ---
# scale: 25%
# name: argo
# ---
# Map of the position of operational Argo floats as of July 2020.
# ```
# 
# ## 1. Load the Data
# 
# The first thing we need to do is import NumPy and Matplotlib. See if you can remember the syntax for importing these packages.

# In[1]:


# import packages
import numpy as np
from matplotlib import pyplot as plt


# Now, let's load the file. The `.npz` file format is a NumPy file format, so we can easily load this file using the `np.load()` function. Note that the raw Argo data does not come in such a nice file format - I made this part a bit easy for us :)

# In[2]:


# Load data
argo = np.load('argo_float_4901412.npz')


# ## 2. Preliminary Data Exploration
# 
# We can examine the data using some simple commands. Note that `.npz` files store NDarrays in a dictionary format. We can identify the different dictionary categories, using the below command.

# In[3]:


# Display data categories
print(argo.files)


# So, we have seven categories. **S** is for salinity, **T** is for temperature and **P** is for pressure.
# 
# We can access the array in each category just as we did for dictionaries.

# In[4]:


print(argo['T'])


# This looks like a lot of data. Let's take a look at the shape of the `T` array.

# In[5]:


print(argo['T'].shape)


# Ok, it looks like we have a 2-D array. What do those two dimensions correspond to? See if you can try to figure out what these dimensions correspond to by printing out the shape of other variables. Click below to check your answer.

# In[6]:


# Shape of array in 'levels' category
print(argo['levels'].shape)

# So, it looks like one of the dimensions corresponds to the number of pressure levels (i.e., the depth of the float).
# Let's take a closer look. What does `levels` look like?

print(argo['levels'])


# In[7]:


# We see that we simply have a set of consecutively numbered levels.
# What about the other dimension? 

# Shape of array in 'date'
print(argo['date'].shape)

# The other dimension corresponds to `date`!

# data in 'date'
print(argo['date'])


# In[8]:


# Looking at the dates, we see that data is collected every 20 days.

# Finally, what are the dimensions of the remaining variables?

# shape of remaining variables
print(argo['S'].shape)
print(argo['P'].shape)
print(argo['lat'].shape)
print(argo['lon'].shape)


# Ok, so now we have a sense of how our data is organized. Often we know this before we even load the data, but sometimes we don't.
# 
# Let's perform a few other NumPy operations on data to get a sense of what our data looks like. For example, let's find the maximum temperature value in our data set.

# In[9]:


# find the maximum
print(np.max(argo['T']))

# alternative way to find the maximum
print(argo['T'].max())


# Oops! Why are we getting `nan` (not-a-number) as the output? This usually means that there are invalid entries within column `T`.
# 
# If we examine the `T` column, you should see some entries are nan.

# In[10]:


print(argo['T'])


# We cannot proceed until this issue is resolved because many NumPy functions do not work properly if arrays contain `nan` values. We have a few options:
# 
# * Delete `nan` entries? You can’t delete the invalid entry, that will mess up the shape.
# * Manually assign place-holder values? This can be tedious.
# 
# NumPy offers a convenient approach to dealing with `nan` values: We can use something called [**Masked Arrays**](https://numpy.org/doc/stable/reference/maskedarray.generic.html).
# 
# ### 2.1 Masked Arrays
# 
# Here we will "mask" out the invalid or `nan` values.

# In[11]:


# mask nan values
T = np.ma.masked_invalid(argo['T'])
print(T)


# Above command will create a new masked array called T with all invalid entries masked (--).
# 
# The mask is simply an array with same shape as the originial data, with 0 and 1 as values. If value is 1, then corresponding data will be ignored.
# 
# Let's look at masked arrays in a bit more detail using a simple example.

# In[12]:


# create a 1-D array with a nan value
mx = np.array([1,2,3,np.float('nan'),5])
print(mx)


# If we try to compute the mean, for example, what will we get?

# In[13]:


# calculate the mean of mx
print(mx.mean())


# We get a meaningless answer.
# 
# Instead, let's create a mask that will tell NumPy to ignore the element with the `nan` value.

# In[14]:


# create a masked array
mx = np.ma.masked_array(np.array([1,2,3,4,5]), mask=[0, 0, 0, 1, 0])
print(mx)


# Now, what happens when we try to compute the mean?

# In[15]:


print(mx.mean())


# Masked arrays are very powerful and can help to save a lot of time when dealing with missing data.

# Ok, now back to our Argo data. We can now mask out all the `nan` values!

# In[16]:


# mask nan values
T = np.ma.masked_invalid(argo['T'])
S = np.ma.masked_invalid(argo['S'])
P = np.ma.masked_invalid(argo['P'])
lat = np.ma.masked_invalid(argo['lat'])


# ## 3. Plotting the Data
# 
# First, let's plot some simple time series of our data. Time series are line plots with time on the x-axis and the variable of interest on the y-axis. 
# 
# To plot time series of this data, we have to pick a level that we are going to plot. Let's pick the surface (level 0) and a level at-depth (level 60) and plot time series of `T` and `S`.
# 
# Before you click to reveal, try this on your own. Once you have something, first click to reveal the output and see if your plot looks similar to mine. If you're stuck, click to reveal the code.

# In[17]:


# define figure size
plt.figure(figsize=(15,5))

# subplot 1
plt.subplot(1,2,1)
plt.plot(argo['date'],T[0,:],label = 'Surface')
plt.plot(argo['date'],T[60,:],label = str(np.round(np.mean(P[60,:]))) + ' db')
plt.title('Temperature (Float 4901412)')
plt.ylabel('$^{\circ}$C') # note: special syntax is required to make symbols
plt.legend(loc = 'upper left')

# subplot 2
plt.subplot(1,2,2)
plt.plot(argo['date'],S[0,:])
plt.plot(argo['date'],S[60,:])
plt.title('Salinity (Float 4901412)')
plt.ylabel('psu')


# Do you see the seasonal cycle in the surface temperature data? Cool!
# 
# Now, let's do a scatter plot. A *T-S* plot is a common way to plot ocean properties. Try it on your own: google "matplotlib scatter plot" to find the command.

# In[18]:


# create a scatter plot
plt.scatter(S, T, c=P) # color corresponds to P, pressure


# ### 3.1 More Plotting Options
# Let's play around with matplotlib! It is more powerful than you think. 
# 
# Try to style your scatter plot above:
# 
# * add labels to your x- and y-axes.
# * add a title
# * add a colourbar
# * add units to your colourbar
# * change the size of your figure
# * make your font larger
# 
# If you get stuck, click to reveal.

# In[19]:


# Plot with title, labels and color bar

# change font size
plt.rcParams.update({'font.size': 14})

# define figure size
plt.figure(figsize=(8,6))

# scatter plot
plt.scatter(S, T, c=P)

# title, labels, colourbar
plt.title("T-S Plot (Float 4901412)")
plt.xlabel("psu")
plt.ylabel("$^{\circ}$C")
plt.colorbar(label = "db") # Add color bar
plt.show()


# ## 4. Simple Statistical Analysis
# 
# Finally, let's do a bit of statistical analysis of our data. NumPy has several [statistical functions](https://numpy.org/doc/stable/reference/routines.statistics.html) that we can use.
# 
# Let's see whether there is a clear relationship between latitude and surface salinity, i.e. does the surface salinity change as the float travels northward? 
# 
# To investigate this, let's first do a scatter plot of these two variabiles. Try on your own first.

# In[20]:


# Plot with title, labels and color bar

# change font size
plt.rcParams.update({'font.size': 14})

# define figure size
plt.figure(figsize=(8,6))

# scatter plot
plt.scatter(argo['lat'], S[0,:])

# title, labels, colourbar
plt.title("Surface Salinity versus Latitude (Float 4901412)")
plt.xlabel("latitude")
plt.ylabel("psu")
plt.show()


# Looks like there is a fairly linear relationship between latitude and surface salinity with salinity decreasing the further north the float travels.
# 
# Let's fit a line to this relationship using `np.polyfit()` and `np.polyval()`. 
# 
# * `np.polyfit(x,y,n)` takes in the predictor (`x`), predictand (`y`) and fits a polynomial of degree-`n`. A straight line is a polynomial of degree-1. The output of this function are the coefficients of the fit (`a`).
# * `np.polyval(a,x)` takes in the coefficients of the fit (`a`) and the predictor (`x`) and outputs the new fitted `y` values.

# In[21]:


# Fit a line (note: we will use np.ma.polyfit because S is a masked array)

a = np.ma.polyfit(argo['lat'],S[0,:],1) # finds the slope and y-intercept for the best-fit line

# Find the new values of the line
S_fit = np.polyval(a,argo['lat'])


# We usually also want to know how robust our linear fit is. To do this we want the *R*-squared value. This tells us what fraction of the variance in `S` if explained by `lat`.
# 
# Using NumPy, we can do this using the `np.corrcoef()` function, which computes the correlation matrix (**R**).

# In[22]:


# calculate the correlation between lat and S
r = np.ma.corrcoef(argo['lat'],S[0,:])
print(r)


# We want the off-diagonal values. Thus, *R*-squared will just be the squared value of *R*.

# In[23]:


# compute the R**2
Rsq = r[0,1]**2
print(Rsq)


# Wow! Latitude explains about 74% for the variance in surface salinity. 
# 
# Now, let's add the linear fit and the *R*-squared information to our plot (as text). Try it on your own first.

# In[24]:


# Plot with title, labels and color bar

# change font size
plt.rcParams.update({'font.size': 14})

# define figure size
plt.figure(figsize=(8,6))

# scatter plot
plt.scatter(argo['lat'], S[0,:])

# add linear fit
plt.plot(argo['lat'], S_fit, label='linear fit (R$^2$ =' + str(np.round(Rsq*100,2)) +'%)')

# title, labels, colourbar
plt.title("Surface Salinity versus Latitude (Float 4901412)")
plt.xlabel("latitude")
plt.ylabel("psu")
plt.legend(loc="upper right")
plt.show()


# This is just a quick sampling of what you can do with NumPy. More sophisticated statistical and numerical analysis can be done with other Python packages, such as [SciPy](https://www.scipy.org/) and [statsmodels](https://www.statsmodels.org/stable/index.html).
# 
# Now, it's your turn to try some simple plotting and analysis.
