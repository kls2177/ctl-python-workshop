#!/usr/bin/env python
# coding: utf-8

# ## Exercises: Part II
# 
# Here we will use what we've learned to remove missing data from a list. As boring as this sounds, managing missing data is a very common issue in scientific computing. So, let's give it a try. 
# 
# In the example below, we have bunch of data that we want to add together but some is missing. Missing data points are flagged with the number -99, so if we include this data in our sum, the results will be incorrect. We want to remove these from our data set before we do our sum.
# 
# We will be reading in a file called `missing_data.csv`. You can download the file [here](https://github.com/kls2177/ccia_files/blob/master/missing_data.zip?raw=true). To read this in, we are going to cheat and use a **package** called **csv**. You can read it in without this package, but it is a bit cumbersome. In Module 2, we will learn more about importing packages.

# In[1]:


# import csv package
import csv

# read in data using csv
with open('missing_data.csv') as f:
    reader = csv.reader(f,delimiter=',')
    sample = list(reader)[0]

print(sample)


# You should be able to see the -99 values in the data above. 
# 
# Let's check what data structure `sample` is. Is it a list, a dictionary, a tuple?

# In[2]:


# check type of data structure using type()


# Now, let's check the type of data in `sample`. Use indexing and type() to do this.

# In[3]:


# pick an element of sample and find the data type


# Now, let's try to remove the missing data and compute the sum using a `for` loop. We should have two new things at the end of our loop, a new list with no missing data and a sum that excludes the missing data.

# In[4]:


# remove missing data and sum
sample_sum = 0  # initialize sum
new_sample = [] # initialize new list

# loop over elements of sample (remove the number sign below to get started)
#for s in sample:
    


# Try it on your own before you click to reveal the answer below. Note that this is an answer - you may have written the code differently but got the correct output. This is fine.

# In[5]:


# remove missing data and sum
sample_sum = 0
new_sample = []

# loop over elements of sample
for s in sample:
    s = int(s) # note we need to do a type conversion!
    if s == -99:
        sample_sum = sample_sum
        new_sample = new_sample
    else:
        sample_sum += s
        new_sample.append(s)

print(sample_sum, new_sample)


# Now, let's try the same thing but write it as a function. Again, try it on your own before you click to reveal.

# In[6]:


# function to remove missing data and compute the sum (remove the number sign below to get started)

#def manage_missing_data(l):
    


# In[7]:


# function to remove missing data and compute the sum 
def manage_missing_data(l):
    sample_sum = 0
    new_sample = []

    # loop over elements of sample
    for s in sample:
        s = int(s)
        if s == -99:
            sample_sum = sample_sum
            new_sample = new_sample
        else:
            sample_sum += s
            new_sample.append(s)
    return sample_sum, new_sample

# call function
print(manage_missing_data(sample))


# Finally, let's suppose that we want to keep both data sets, the one with missing values and the one without, and store them in a dictionary. How would you construct this dictionary?

# In[8]:


# Dictionary of data
all_data = {'original': sample, 'no missing': new_sample}
print(all_data)


# If you want more practice, check out the following [link](https://www.practicepython.org/). You can also google "python exercises beginner" to find many more links (e.g. here's another [one](https://www.w3resource.com/python-exercises/)).

# In[ ]:




