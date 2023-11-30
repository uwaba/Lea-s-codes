#!/usr/bin/env python
# coding: utf-8

# In[1]:


import Preprocessing
import Insole_Separation as sep
import FeatureExtraction
import DatabaseManage
import MLClassification as ml
import os


# In[2]:


### read, smooth and select parts of 1 step
def processingOneStep(file, factor, numFeatures):
    #url= 'C://DFKI//Insole//Daten//SchrittePers3//5.csv'
    url=file
    #print("Processing Data of file : {}".format(file))
    # separate the data into time frames
    dataframes= Preprocessing.separateData(url)
    #print(f"dataframes:{dataframes}")
    #print("Data is smoothed with factor {}".format(factor))
    # smooth data to remove outliers
    smooth_dataframes2= Preprocessing.smooth_data2(dataframes,factor)
   # smooth_dataframes2[0][1].style.background_gradient(cmap='Blues')

    #print("Chosen parts of the matrix are extracted")
    if numFeatures==1:
        partDicts= sep.extract1Part(smooth_dataframes2)
    elif numFeatures==2:
        partDicts= sep.extract2Parts(smooth_dataframes2)
    elif numFeatures==3:
        partDicts= sep.extract3Parts(smooth_dataframes2)
    elif numFeatures==4:
        partDicts= sep.extract4Parts(smooth_dataframes2)
    elif numFeatures==5:
        partDicts= sep.extract5Parts(smooth_dataframes2)
    elif numFeatures==9:
        partDicts= sep.extract9Parts(smooth_dataframes2)
   # print(partDicts[0])
    features= FeatureExtraction.extractFeatures(partDicts)
    #print("Feature Extraction finished")
    return features


# In[3]:


# url of the step, factor for smoothing, number of features to extract and number of steps to merge into 1 step features
def processSteps(url, factor, numFeatures):
    
    
    #print("\n\n")
    # list of features for one set of a person, contains lists, which contain lists (for each step one) with    first elemm: list with time stamps, seconnd elem: lists with features (as many as matrices for one step exist)
    listOfFeatures= []
    for el in os.listdir(url):
        file= url + el
        features= processingOneStep(file, factor, numFeatures)
        listOfFeatures.append(features)
        
        
    # create a list for all features for each step
    #print("\n Separate Step into 8 Phases and the additional Feature")
    #print(listOfFeatures)
    ## Use this line instead of line
    stepFeatures= FeatureExtraction.createFeatureListForSteps(listOfFeatures)
    #print(f"list of features: {stepFeatures}")
    #print("\n\n")
    #stepFeatures= FeatureExtraction.mergeSteps(listOfFeatures, numFeatures, numberSteps)
    return stepFeatures


# In[ ]:




