#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# use **jupyter nbconvert --to script HelpFunctions.ipynb**
# to convert notebook to script

# In[2]:


def replace_none_with_zero(lst):
    for i in range(len(lst)):
        if isinstance(lst[i], list):
            replace_none_with_zero(lst[i])  # Recursively call the function for nested lists
        elif lst[i] is None:
            lst[i] = 0


# In[3]:


def replace_inf_with_zero(lst):
    for i in range(len(lst)):
        if isinstance(lst[i], list):
            replace_inf_with_zero(lst[i])  # Recursively call the function for nested lists
        elif math.isinf(lst[i]):# is float('inf')) or (lst[i] is float('-inf')):
            lst[i] = 0


# In[4]:


def round_float_to_int(lst):
    for i in range(len(lst)):
        if isinstance(lst[i], list):
            round_float_to_int(lst[i])  # Recursively call the function for nested lists
        elif isinstance(lst[i], float):
            lst[i] = round(lst[i])

