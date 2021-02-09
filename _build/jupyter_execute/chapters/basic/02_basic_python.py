#!/usr/bin/env python
# coding: utf-8

# # Part II: Loops, Data Structures and Functions
# 
# In Part II, we will cover a few more programming basics (e.g. loops, functions, etc.) and learn about python-specific [data structures](https://docs.python.org/3/tutorial/datastructures.html). 

# ## 5. Loops
# 
# Loops are important in programming as they allow you to execute a block of code repeatedly. It is very common that you may need to use a piece of code over and over but you do not want to write the same line of code multiple times.
# 
# There are two types of loops:
# 
# * `while` loops
# * `for` loops
# 
# ### 5.1 While Loops
# While loops in Python follow the following format:
# ```
# while expression:
#     command1
#     command2
#     ...
# ```
# Commands will keep executing until `expression` becomes False equivalent. Again, note the **syntax** - the expression is followed by a colon and the commands are indented.
# 
# Take a look at the while loop below. What do you think the output will be? 

# In[1]:


# A simple while loop
i = 10
while i:
    print(i**i)
    i = i - 1


# Note that `i -= 1` is a shortcut for `i = i - 1`.

# ### 5.2 For Loops
# You can use `for` loops to loop through a `range` of values. Later you will see it can also loop through lists.
# ```
# for value in range(int):
#     command1
#     command2
#     ...
# ```
# 
# Before we proceed, let's see how the `range()` function works (another built-in python function).
# 
# `range(start, stop, step)` creates a range of integers from *start* up to but not including *stop*. *start* is optional and defaults to zero. *step* is also optional: the default is 1. 
# 
# This will loop and set `value` from 0 until `int - 1`.

# In[2]:


# A simple while loop (demonstration of range function)
for value in range(10):
    print(value)


# In[3]:


# A simple while loop identifying even (0) and odd (1) numbers
for value in range(10):
    print(value % 2)


# ## 6. Lists
# Now, for the fun stuff! We rarely want to just work with one number at a time. We often want to store more than one thing in the same data structure. You can store anything in a list. 
# 
# To create a list, use the following command:
# ```python
# l = [] # l is now an empty list
# ```
# You can also pre-populate the *elements* of the list:
# ```python
# l = [1, 2, "hello"]
# ```

# In[4]:


# Create an empty list
l = []
print(l)


# In[5]:


# Create a list with different data types
l = [1, 2.3, "hello"]
print(l)


# ### 6.1 List Operations
# There are many list operations you could do, following are just some basic examples.

# In[6]:


# Append: add an element to a list
l = [1, 3.4, "test"]
l.append("hi")
print(l)


# In[7]:


# Pop: remove an element from a list
l = [1, 3.4, "hi"]
print(l.pop())
print(l)


# If we want to access an element of a list, we can use **indexing**. Indices start from zero in python. 
# 
# So, in the example below, if we are accessing element 1, what value are we going to get?

# In[8]:


# Access a value by index. Python counts from 0!
l = [1, 3.4, "123"]
print(l[1])


# In[9]:


# Concatenate two lists with a + sign
a = [1,2]
b = [3,4]
print(a + b)


# #### More List Operations
# * list.sort()
# * list.remove()
# * list.clear()
# * list.reverse()
# * ...
# 
# Here are even [more](https://www.w3schools.com/python/python_lists.asp)!

# ### 6.2 Extract Data From Lists
# [**Slicing**](https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/) is a term used for extracting a subset of elements from a list in python. These can be very confusing, so spend some time thinking about the slices before revealing the output and play around with these in your own jupyter notebook.

# In[10]:


# Elements after index (inclusive): start from the second element and go to the end (:)
l = [1,2,3,4,5,6,7]
print(l[2:])


# In[11]:


# Elements before index (exclusive): start from the beginning and go to element 2 (up to but not including 3)
l = [1,2,3,4,5,6,7]
print(l[:3])


# In[12]:


# Negative index (access from end)
l = [1,2,3,4,5,6,7]
print(l[-1])


# In[13]:


# Elements between two indexes: start at element 2 and go to element 5 (up to but not including 6)
l = [1,2,3,4,5,6,7]
print(l[2:6])


# ### 6.3 Loop Through a List
# Now, let's use what we learned about loops to loop through a list. 
# 
# In the example below, what will be the output? Try it out on your own or click to reveal the output.

# In[14]:


# Loop through a list
l = [1,3,6,"hi"]
for element in l:
    print(element)


# An alternative way to loop through a list is to use indexing. Here we are using another built-in python function, `len()` to find the number of elements in a list. How many elements are in the list below?

# In[15]:


# demonstration of the len() function
l = [1,3,6,"hi"]
print("There are " + str(len(l)) + " elements in l")


# In[16]:


# Loop through a list
l = [1,3,6,"hi"]
for i in range(len(l)):
    print(l[i])


# ## 7. Tuples
# Tuples are like lists, but immutable. We will take a closer look at what immutable means later.
# 
# To create a tuple, use the following command:
# ```python
# t = () # t is now an empty tuple
# ```
# You can also pre-populate the *elements* of the tuple:
# ```python
# t = (1, 2, 3)
# ```

# In[17]:


# Create an empty tuple
t = ()
print(t)


# In[18]:


# Create a tuple
t = (1,2,3)
print(t)


# In[19]:


# loop over elements of t
t = (1,2,3)
for element in t:
    print(element)


# ## 8. Dictionaries
# Instead of having an numeric index for each value, dictionaries allow you to map a custom key to each value. You can think of dictionaries like spreadsheets, with the keys being the column names. You can use almost anything as a key, it is quite flexible.
# 
# To create a dictionary, use the following command:
# ```python
# d = {} # d is now an empty dictionary
# ```
# You can also pre-populate the *keys* and *elements* of the dictionary:
# ```python
# d = {'name': "Jun", 'age': 20}
# ```
# where the keys are `name` and `age` and the elements are *Jun* and *20*.

# In[20]:


# Create an empty dictionary
d = {}
print(d)


# In[21]:


# Create a dictionary
d = {
    'name': "Jun",
    'age': 20,
    True: 'yes',
    4: 5,
    False: (7,8)
}
print(d)


# ### 8.1 Dictionary Operations
# Below are some basic dictionary operations you could use.
# 
# In the example below, which is the key and which is the element?

# In[22]:


# Add value to a key
d = {}
d['test'] = 123
print(d)


# In[23]:


# Access values for a key
d = {'test': [123, "hello"]}
print(d['test'])


# What if you want just one element for a specific key? Again, you can use indexing. In the example below, which element will be printed?

# In[24]:


# Access values for a key
d = {'test': [123, "hello"]}
print(d['test'][1])


# ### 8.2 Loop Through Dictionaries
# You can loop through dictionaries using a for loop.
# 
# **Dictionaries are unorderd.** Thus the output order cannot be guaranteed.

# In[25]:


# loop through a dictionary
d = {
    'name': "Jun",
    'age': 20,
    True: 'yes',
    4: 5,
    False: (7,8)
}
for key in d:
    print(key, d[key])


# ## 9. Functions
# Functions allow you to break your program into pieces. They also enable the ability to reuse code, similar to loops. 
# 
# You define functions using following syntax:
# ```
# def function_name(input_1, input_2):
#     command1
#     command2
#     return output
# ```
# 
# Once a function returns, it will immediately exit the function.
# 
# The function is defined and then it needs to be called with actual input. Let's take a look.

# In[26]:


# Define a simple function that has input, name 
def hi(name):
    return "hi " + str(name)


# What will the output of the function be for the input below?

# In[27]:


# Call the function
print(hi("Jun"))


# Sometimes, we want to specify a default input so that the function will always work even if no input is provided. Here is an example.

# In[28]:


# Slightly modified simple function: default input
def hi(name="Jun"):
    return "hi " + str(name)

# Call the function
print(hi())


# Now, modify the above call and specify your own name as the input. What happens?
# 
# For some functions, we may not know how many inputs there will be. In this case, we can allow for a flexible number of inputs. Try modifying the inputs and see what happens. 

# In[29]:


# A function with flexible number of inputs (computes the sum of a set of numbers)
def get_sum(*input):
    result = 0 # initialize the variabile result
    for num in input:
        result += num # this is a short-cut for result = result + num
    return result

# Call function
print(get_sum(1,2,3,-1,90))


# ## 10. Mutable & Immutable Types
# 
# As you can probably guess, a mutable object can be changed after it is created, and an immutable object can not.
# 
# * Mutable
#     * List, Dictionary
# * Immutable
#     * Integer, Float, String, Boolean, Tuple
#     
# The best way to explore mutable and immutable types is with an example. Take a look at the function below. What will the output be for list, l?

# In[30]:


# What will happen?
def weird_function(l):
    l[0] = 'interesting'

# Call function
l = [1,2,3]
weird_function(l)
print(l)


# Now, let's try the same thing, but with a tuple (an immutable data structure). What happens?

# As you can see, the function "mutated" the original list. However, if we change the list to a tuple...
# 
# ```{figure} tuple.png
# ---
# height: 150px
# name: tuple
# ---
# ```
# 
# The function is not able to mutate the tuple - we get an error. 

# Now, we will test what we've learned by cleaning up missing data in a list.

# In[ ]:




