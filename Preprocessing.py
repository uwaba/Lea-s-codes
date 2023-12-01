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


# Time Frame Separation for 1 Step

# In[1]:


# separates the data of a step into time frames
def separateData(url):
    col_names = ["col1", "col2", "col3", "col4", "col5", "col6"]
    data = pd.read_csv(url, encoding = 'ISO-8859-1', lineterminator='\n', names=col_names)
    #print(data)


    ### add new column with step number
    times= 0*len(data)
    data["time"]= times


    ### 1. find new time beginnings

    newTimeLines= data.loc[data['col1'].str.contains("MS", na=False)].index
    time= data.loc[data['col1'].str.contains("MS", na=False)]['col1'].str.partition("MS:")[2].str.partition(" M")[0]
    times=[]
    for val in time:
        times.append(val)
    #times=list(time.var())
    #dataframes= []
    # list with no headlines
    dataframes2=[]
    ind=0
    ind2=0
    ind1=0
    var=0

    for line in newTimeLines:
        #print(line,ind1)
        #print(line-ind1)
        # test if the time matrix is complete
        if((line-ind1)==13):
            # add the corresponding time to the dataframe
            data.iloc[ind1:line, [6]]=times[ind2]
            #print(times[ind2])
            ind2+=1
            #dataframes.append(data.iloc[ind1:line, : ])
        
            dataframes2.append(data.iloc[ind1:line, : ].tail(data.iloc[ind1:line, : ].shape[0]-1))
            

            
        ind1=line
        ind+=1
    #print(dataframes2)
    #smooth_dataframes= smooth_data(dataframes,1)
    return dataframes2


# Smooth given dataframes with a gaussian filter to remove outliers

# In[2]:


## smooth data full implementation
# param: list of dataframes for 1 step, factor for smoothing
# return: list of smoothed dataframes
def smooth_data2(dataframes, fac):
    warnings.filterwarnings('ignore')
    
    # faktor wie stark die daten angepasst werden
    intensity=5
    # if smoothing factor is 0 don't change anything
    smooth_dataframes=[]
    
    if fac == 0:
        
        for df in dataframes:
            try:
                time=df['time']
                print(time)
                df= df.drop('time', axis=1)
                print(df)
                t= float(time.iloc[0])
                print(t)
                li=[]
                li.append(t)
                li.append(df)
                smooth_dataframes.append(li)
            except:
                print("error in smooth, throw dataframe away")
            
    else:
        #factor= 1/fac
        factor = fac
            
        index=range(1,19)
        # interate over dataframes:
        for df in dataframes:
            try:
                time=df['time']
                    # print(time)
                df= df.drop('time', axis=1)
                    # print(df)
                # create new dataframe for smoothed data
                df_new = pd.DataFrame(index= index, columns= ["col1", "col2", "col3", "col4", "col5", "col6"])
                df_new = df_new.fillna(0) # with 0s rather than NaNs
                    
                # copy first and last row
                df_new.iloc[0] = df.iloc[0]
                df_new.iloc[-1] = df.iloc[-1]
                    
                # smooth data in each column
                    #df = big data frame
                shape = (3,3) #shape of matrix to be analyzed
                step = 1 #step size, iterate over every number
                #you can set step = shape if you are working  with a matrix that isn't square, just be sure to change step in the code below to step[0] and step[1] respectively 
                for row in range( 0, len(df) - shape[0]+1, step): #number of rows of big dataframe - number of rows of matrix to be analyzed 
                    for col in range(0, len(df.iloc[0,:]) - shape[1]+1, step): #number of columns of big dataframe - number of columns of matrix to be analized 
                        matrix = df.iloc[row:shape[0]+row, col:shape[1]+col] #slice out matrix and set it equal to 'matrix'
                            # print(matrix)
                        mean=matrix.mean(axis=1).mean()
                            #print(matrix.mean(axis=1).mean())
                            #print(df.iloc[row+1:shape[0]+row-1, col+1:shape[1]+col-1])
                        # middle value
                        mw= matrix.iloc[1:2,1:2]
                        # check for edges
                        if 'col1' in matrix:
                                # calc smaller mean value
                            smallM= matrix.iloc[:2, :2]
                                #print(smallM) 
                            meanS= smallM.mean(axis=1).mean()
                            mwS= matrix.iloc[0:1,0:1]
                                #print('mwS')
                                #print(float(mwS.values[0]))
                                
                            if float(mwS.values[0])> (meanS+ factor*intensity):
                                #   print('bigger')
                                df_new.iloc[row:shape[0]+row-2, col:shape[1]+col-2]= meanS+ factor*intensity
                            elif float(mwS.values[0])< (meanS - factor*intensity):
                                    #  print('smaller')
                                df_new.iloc[row:shape[0]+row-2, col:shape[1]+col-2]= meanS- factor*intensity
                            else:
                                df_new.iloc[row:shape[0]+row-2, col:shape[1]+col-2]= mwS
                        if 'col6' in matrix:
                                # calc smaller mean value
                            smallM= matrix.iloc[0:2, 1:3]
                                # print(smallM) 
                            meanS= smallM.mean(axis=1).mean()
                            mwS= matrix.iloc[0:1,2:]
                                #   print('mwS')
                                #  print(float(mwS.values[0]))
                                # print(df.iloc[row:shape[0]+row-2, col+2:shape[1]+col])
                                    
                            if float(mwS.values[0])> (meanS+ factor*intensity):
                                    #    print('bigger')
                                df_new.iloc[row:shape[0]+row-2, col+2:shape[1]+col]= meanS+ factor*intensity
                            elif float(mwS.values[0])< (meanS - factor*5):
                                    #   print('smaller')
                                df_new.iloc[row:shape[0]+row-2, col+2:shape[1]+col]= meanS- factor*intensity
                            else:
                                df_new.iloc[row:shape[0]+row-2, col+2:shape[1]+col]= mwS
                                    
                                    
                        if mw.values[0]> (mean+ factor*intensity):
                                    #print('bigger')
                            df_new.iloc[row+1:shape[0]+row-1, col+1:shape[1]+col-1]= mean+ factor*intensity
                        elif mw.values[0]< (mean - factor*intensity):
                                    #print('smaller')
                            df_new.iloc[row+1:shape[0]+row-1, col+1:shape[1]+col-1]= mean- factor*intensity
                        else:
                            df_new.iloc[row+1:shape[0]+row-1, col+1:shape[1]+col-1]= mw
                                #analyze matrix here 
                        #df_new['time']= time.iloc[0]
                #print(type(float(time.iloc[0])))
                t= float(time.iloc[0])
                #print(df_new)
                li=[]
                li.append(t)
                li.append(df_new)
                smooth_dataframes.append(li)
                    #print(smooth_dataframes)
                start= index[-1]+2
                end= start+12
                index=range(start, end)
            except:
                print("error in smooth, throw dataframe away")
   
    # if smoothing factor is 0 don't change anything
    #except:
       # smooth_dataframes=dataframes
       
    #print(smooth_dataframes)
    return smooth_dataframes  

