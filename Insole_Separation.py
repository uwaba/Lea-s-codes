#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import scipy
import warnings
import math
warnings.filterwarnings('ignore')


# use **jupyter nbconvert --to script Insole_Separation.ipynb**
# to convert notebook to script

# Extract specific parts of the insole for the later feature extraction (e.g. toes, heel, etc.)

# In[2]:


## toes1, toes2, toes3, toes4, toes5 , ball, lenLeft, lenRight, heel

######## 
# dictionary parts can be changes to extract features (both must include the same variables)
#################################


# extract parts of the dataframe based on insole for 1 step
# parts:    toes        = 1-2
#           ball of foot= 3-5
#           length      = 6-9 (jeweils in 3er spalten)
#           heel        = 10-12

def extract9Parts(frames):
    # dict to split into rows
    # values are the last row of this part
    parts= {
        'toes1':2,
        'toes2':2,
        'toes3':2,
        'toes4':2,
        'toes5':2,
        'ball':5, 
        'lenLeft': 9, 
        'lenRight':9,
        'heel':12
    }


    # dict to split into columns
    # same keys as dict
    # values are the last column of the part
    split={
        'toes1':2,
        'toes2':3,
        'toes3':4,
        'toes4':5,
        'toes5':6,
        'ball':6,
        'lenLeft': 3,
        'lenRight':6,
        'heel':6
    }

    # go through 1 step and create a list of dataframes for each time
    partDicts=[]

    i=0
    for list in frames:

        # split dataframe into parts
        ind=0
        sp=0
        partList= parts.keys()
        #print(partList)
        # append time to the first list
        #print("list[0] : {}".format(list[0]))
        partDicts.append([list[0]])
        for p in partList:
            # dataframes[framenumber][1]
            partDicts[i].append(list[1].iloc[ind:parts[p],sp:split[p]])    
            #print(list[1].iloc[ind:parts[p],sp:split[p]])
            
            sp = split[p]
            if sp == 6:
                sp = 0
                ind = parts[p]
            
            # append right divided by left:
            #partDicts[i].append(list[1].iloc[:,0:3].median().median()/ list[1].iloc[:,3:6].median().median())
        #partDicts[i].append(list[1])
            #print(list[1].iloc[:,0:3].median().median()/ list[1].iloc[:,3:6].median().median())
        #print("number {}".format(i))
        #print(partDicts[i])   
        i+=1
    return partDicts


# In[3]:


## toes, ball, lenLeft, lenRight, heel

#######
# adjust the dictionaries parts and split to extract features (both must include the same variables)
#################################


# extract parts of the dataframe based on insole for 1 step
# parts:    toes        = 1-2
#           ball of foot= 3-5
#           length      = 6-9 (jeweils in 3er spalten)
#           heel        = 10-12

def extract5Parts(frames):
    # dict to split into rows
    # values are the last row of this part
    parts= {
        'toes5':2,
        'ball':5, 
        'lenLeft': 9, 
        'lenRight':9,
        'heel':12
    }


    # dict to split into columns
    # same keys as dict
    # values are the last column of the part
    split={
        'toes5':6,
        'ball':6,
        'lenLeft': 3,
        'lenRight':6,
        'heel':6
    }

    # go through 1 step and create a list of dataframes for each time
    partDicts=[]

    i=0
    for list in frames:

        # split dataframe into parts
        ind=0
        sp=0
        partList= parts.keys()
        #print(partList)
        # append time to the first list
        #print("list[0] : {}".format(list[0]))
        partDicts.append([list[0]])
        for p in partList:
            # dataframes[framenumber][1]
            partDicts[i].append(list[1].iloc[ind:parts[p],sp:split[p]])    
            #print(list[1].iloc[ind:parts[p],sp:split[p]])
            
            sp = split[p]
            if sp == 6:
                sp = 0
                ind = parts[p]
            
            # append right divided by left:
            #partDicts[i].append(list[1].iloc[:,0:3].median().median()/ list[1].iloc[:,3:6].median().median())
        #partDicts[i].append(list[1])
            #print(list[1].iloc[:,0:3].median().median()/ list[1].iloc[:,3:6].median().median())
        #print("number {}".format(i))
        #print(partDicts[i])   
        i+=1
    return partDicts


# In[4]:


## toes, lenLeft, lenRight, heel




# extract parts of the dataframe based on insole for 1 step
# parts:    toes        = 1-2
#           ball of foot= 3-5
#           length      = 6-9 (jeweils in 3er spalten)
#           heel        = 10-12

def extract4Parts(frames):
    # dict to split into rows
    # values are the last row of this part
    parts= {
        'ball':5, 
        'lenLeft': 9, 
        'lenRight':9,
        'heel':12
    }


    # dict to split into columns
    # same keys as dict
    # values are the last column of the part
    split={
        'ball':6,
        'lenLeft': 3,
        'lenRight':6,
        'heel':6
    }

    # go through 1 step and create a list of dataframes for each time
    partDicts=[]

    i=0
    for list in frames:

        # split dataframe into parts
        ind=0
        sp=0
        partList= parts.keys()
        #print(partList)
        # append time to the first list
        #print("list[0] : {}".format(list[0]))
        partDicts.append([list[0]])
        for p in partList:
            # dataframes[framenumber][1]
            partDicts[i].append(list[1].iloc[ind:parts[p],sp:split[p]])    
            #print(list[1].iloc[ind:parts[p],sp:split[p]])
            
            sp = split[p]
            if sp == 6:
                sp = 0
                ind = parts[p]
            
            # append right divided by left:
            #partDicts[i].append(list[1].iloc[:,0:3].median().median()/ list[1].iloc[:,3:6].median().median())
        #partDicts[i].append(list[1])
            #print(list[1].iloc[:,0:3].median().median()/ list[1].iloc[:,3:6].median().median())
        #print("number {}".format(i))
        #print(partDicts[i])   
        i+=1
    return partDicts


# In[5]:


## toes, len,  heel



# extract parts of the dataframe based on insole for 1 step
# parts:    toes        = 1-2
#           ball of foot= 3-5
#           length      = 6-9 (jeweils in 3er spalten)
#           heel        = 10-12

def extract3Parts(frames):
    # dict to split into rows
    # values are the last row of this part
    parts= {
        'ball':5, 
        'lenRight':9,
        'heel':12
    }


    # dict to split into columns
    # same keys as dict
    # values are the last column of the part
    split={
        'ball':6,
        'lenRight':6,
        'heel':6
    }

    # go through 1 step and create a list of dataframes for each time
    partDicts=[]

    i=0
    for list in frames:

        # split dataframe into parts
        ind=0
        sp=0
        partList= parts.keys()
        #print(partList)
        # append time to the first list
        #print("list[0] : {}".format(list[0]))
        partDicts.append([list[0]])
        for p in partList:
            # dataframes[framenumber][1]
            partDicts[i].append(list[1].iloc[ind:parts[p],sp:split[p]])    
            #print(list[1].iloc[ind:parts[p],sp:split[p]])
            
            sp = split[p]
            if sp == 6:
                sp = 0
                ind = parts[p]
            
            # append right divided by left:
            #partDicts[i].append(list[1].iloc[:,0:3].median().median()/ list[1].iloc[:,3:6].median().median())
        #partDicts[i].append(list[1])
            #print(list[1].iloc[:,0:3].median().median()/ list[1].iloc[:,3:6].median().median())
        #print("number {}".format(i))
        #print(partDicts[i])   
        i+=1
    return partDicts


# In[6]:


## lenLeft, lenRight


# extract parts of the dataframe based on insole for 1 step
# parts:    toes        = 1-2
#           ball of foot= 3-5
#           length      = 6-9 (jeweils in 3er spalten)
#           heel        = 10-12

def extract2Parts(frames):
    # dict to split into rows
    # values are the last row of this part
    parts= {
        'lenLeft': 12, 
        'lenRight':12
    }


    # dict to split into columns
    # same keys as dict
    # values are the last column of the part
    split={
        'lenLeft': 3,
        'lenRight':6
    }

    # go through 1 step and create a list of dataframes for each time
    partDicts=[]

    i=0
    for list in frames:

        # split dataframe into parts
        ind=0
        sp=0
        partList= parts.keys()
        #print(partList)
        # append time to the first list
        #print("list[0] : {}".format(list[0]))
        partDicts.append([list[0]])
        for p in partList:
            # dataframes[framenumber][1]
            partDicts[i].append(list[1].iloc[ind:parts[p],sp:split[p]])    
            #print(list[1].iloc[ind:parts[p],sp:split[p]])
            
            sp = split[p]
            if sp == 6:
                sp = 0
                ind = parts[p]
            
            # append right divided by left:
            #partDicts[i].append(list[1].iloc[:,0:3].median().median()/ list[1].iloc[:,3:6].median().median())
        #partDicts[i].append(list[1])
            #print(list[1].iloc[:,0:3].median().median()/ list[1].iloc[:,3:6].median().median())
        #print("number {}".format(i))
        #print(partDicts[i])   
        i+=1
    return partDicts


# In[7]:


## 1 part 



# extract parts of the dataframe based on insole for 1 step
# parts:    toes        = 1-2
#           ball of foot= 3-5
#           length      = 6-9 (jeweils in 3er spalten)
#           heel        = 10-12

def extract1Part(frames):
    # dict to split into rows
    # values are the last row of this part
    parts= {
        'heel':12
    }


    # dict to split into columns
    # same keys as dict
    # values are the last column of the part
    split={
        'heel':6
    }

    # go through 1 step and create a list of dataframes for each time
    partDicts=[]

    i=0
    for list in frames:

        # split dataframe into parts
        ind=0
        sp=0
        partList= parts.keys()
        #print(partList)
        # append time to the first list
        #print("list[0] : {}".format(list[0]))
        partDicts.append([list[0]])
        for p in partList:
            # dataframes[framenumber][1]
            partDicts[i].append(list[1].iloc[ind:parts[p],sp:split[p]])    
            #print(list[1].iloc[ind:parts[p],sp:split[p]])
            
            sp = split[p]
            if sp == 6:
                sp = 0
                ind = parts[p]
            
            # append right divided by left:
            #partDicts[i].append(list[1].iloc[:,0:3].median().median()/ list[1].iloc[:,3:6].median().median())
        #partDicts[i].append(list[1])
            #print(list[1].iloc[:,0:3].median().median()/ list[1].iloc[:,3:6].median().median())
        #print("number {}".format(i))
        #print(partDicts[i])   
        i+=1
    return partDicts

