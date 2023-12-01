#!/usr/bin/env python
# coding: utf-8

# In[2]:


# merge the features of different steps to one list
# function to merge a specific number of steps to one single step
def mergeStepsOLD(featureList, numfeatures, numberSteps): 

    remainingSteps= int(len(featureList)/numberSteps)
    
    newList=[]
    for i in range(remainingSteps):
        newList.append([[0] * numfeatures, [0] * numfeatures, [0] * numfeatures, [0] * numfeatures, [0] * numfeatures, [0] * numfeatures, [0] * numfeatures, [0] * numfeatures])
   
    countSteps=-1
    j=0
    lenCount=0
    # if there are too little steps available
    if len(featureList) < numberSteps:
        print("Error for merging the steps in Feature Extraction. Choose a smaller number of steps, as not enough steps are in the Feature List")
        return []
    
    for liste in featureList:
        countSteps+=1
        
        # if you have enough steps merged then start a new batch
        if(countSteps==numberSteps):
            
            j+=1 
            countSteps=0
            
        i=0
        for teil in liste:
           
            newList[j][i]= [sum(element) for element in zip(newList[j][i],teil)] 
                
            i+=1
        # if there are not enough steps to continue, then stop here
        lenCount+=1
        
        if countSteps==True:
            if (len(featureList)-lenCount < numberSteps):
                
                break
        
        
    for k in range(len(newList)):
        
        for l in range(len(newList[k])):
            
            newList[k][l]= [element/numberSteps for element in newList[k][l]]       
    
    return newList


# In[3]:


# merge the features of different steps to one list
# function to merge a specific number of steps to one single step
def mergeStepsOLD(featureList, numfeatures, numberSteps): 

    remainingSteps= int(len(featureList)/numberSteps)
    
    newList=[]
    for i in range(remainingSteps):
        newList.append([[0] * numfeatures, [0] * numfeatures, [0] * numfeatures, [0] * numfeatures, [0] * numfeatures, [0] * numfeatures, [0] * numfeatures, [0] * numfeatures])
   
    
    #newList= [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    countSteps=-1
    j=0
    lenCount=0
    # if there are too little steps available
    if len(featureList) < numberSteps:
        print("Error for merging the steps in Feature Extraction. Choose a smaller number of steps, as not enough steps are in the Feature List")
        return []
    
    for liste in featureList:
        countSteps+=1
        
        # if you have enough steps merged then start a new batch
        if(countSteps==numberSteps):
            
            j+=1 
            countSteps=0
        # if there are not enough steps to continue, then stop here
        lenCount+=1
        
        if countSteps==0:
            if ((len(featureList)-lenCount) < numberSteps):
                print("done, not enough left")
                break    
            
          
        #print("features:")   
        #print(liste)
        #print(j)
        #print(newList)
        #print(newList[j])
        i=0
        for teil in liste:
            
            newList[j][i]= [sum(element) for element in zip(newList[j][i],teil)] 
                
            i+=1
        
        
    
    for k in range(len(newList)):
        
        for l in range(len(newList[k])):
            
            newList[k][l]= [element/numberSteps for element in newList[k][l]]       
    
    return newList


# use **jupyter nbconvert --to script MergeSteps.ipynb**
# to convert notebook to script

# In[4]:


def mergeSteps(featureList, numfeatures, numberSteps): 

    remainingSteps= int(len(featureList)/numberSteps)
    
    newList=[]
    for i in range(remainingSteps):
        newList.append([[0] * numfeatures, [0] * numfeatures, [0] * numfeatures, [0] * numfeatures, [0] * numfeatures, [0] * numfeatures, [0] * numfeatures, [0] * numfeatures])
   
    
    #newList= [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    countSteps=-1
    j=0
    lenCount=0
    # if there are too little steps available
    if len(featureList) < numberSteps:
        print("Error for merging the steps in Feature Extraction. Choose a smaller number of steps, as not enough steps are in the Feature List")
        return []
    
    for liste in featureList:
        countSteps+=1
        
        # if you have enough steps merged then start a new batch
        if(countSteps==numberSteps):
            
            j+=1 
            countSteps=0
        # if there are not enough steps to continue, then stop here
        lenCount+=1
        
        if countSteps==0:
            if ((len(featureList)-lenCount) < numberSteps):
                print("done, not enough left")
                break    
            
          
        #print("features:")   
        #print(liste)
        #print(j)
        #print(newList)
        #print(newList[j])
        i=0
        for teil in liste:
            
            newList[j][i]= [sum(element) for element in zip(newList[j][i],teil)] 
                
            i+=1
        
        
    
    for k in range(len(newList)):
        
        for l in range(len(newList[k])):
            
            newList[k][l]= [element/numberSteps for element in newList[k][l]]       
    
    return newList


# In[5]:


import random

# function which chooses randomly steps from the feature extraction and adds it to other steps to get a greate feature list 
def appendSteps(featureList, numfeatures, numberSteps): 

    #remainingSteps= int(len(featureList)/numberSteps)
    #print(remainingSteps)
    
    newList=[]
    #for i in range(remainingSteps):
    #    newList.append([[0] * numfeatures, [0] * numfeatures, [0] * numfeatures, [0] * numfeatures, [0] * numfeatures, [0] * numfeatures, [0] * numfeatures, [0] * numfeatures])
   
    countSteps=0
    #j=0
    lenCount=0
    # if there are too little steps available
    if len(featureList) < numberSteps:
        print("Error for adding the steps in Feature Extraction. Choose a smaller number of steps, as not enough steps are in the Feature List")
        return []
    
    currentlist=[]
    
    while len(featureList) >= (numberSteps):
        while countSteps <numberSteps:
            # print(len(featureList))
            # Zufällig eine innere Liste auswählen
            zufall_index = random.randint(0, len(featureList) - 1)
            selected_list = featureList[zufall_index]
            for el in selected_list:
                currentlist.append(el)
            # Die ausgewählte innere Liste aus der Gesamtliste entfernen
            del featureList[zufall_index]
            countSteps+=1
        #if(countSteps==numberSteps):
        newList.append(currentlist)
        #print(f"new list: {newList}")
            #j+=1 
        countSteps=0
        currentlist=[]
         
    return newList

