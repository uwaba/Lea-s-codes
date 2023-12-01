#!/usr/bin/env python
# coding: utf-8

# In[63]:


import sqlite3
from _sqlite3 import Error


# use **jupyter nbconvert --to script DatabaseManage.ipynb**
# to convert notebook to script

# create a connection to the database

# In[64]:


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


# add new features to the database

# In[65]:


def addInsoleFeatures1(db_file, person,step, feature1):
    conn= create_connection(db_file)
    params= (person,step, feature1)
    conn.execute('INSERT INTO insole_features VALUES( ?, ?, ?)', params)
    conn.commit()
    conn.close()


# In[66]:


def addInsoleFeatures2(db_file, person,step, feature1, feature2):
    conn= create_connection(db_file)
    params= (person,step, feature1, feature2)
    conn.execute('INSERT INTO insole_features VALUES( ?, ?, ?, ?)', params)
    conn.commit()
    conn.close()


# In[67]:


def addInsoleFeatures3(db_file, person,step, feature1, feature2, feature3):
    conn= create_connection(db_file)
    params= (person,step, feature1, feature2, feature3)
    conn.execute('INSERT INTO insole_features VALUES( ?, ?, ?, ?, ?)', params)
    conn.commit()
    conn.close()


# In[68]:


def addInsoleFeatures4(db_file, person,step, feature1, feature2, feature3, feature4):
    conn= create_connection(db_file)
    params= (person,step, feature1, feature2, feature3, feature4)
    conn.execute('INSERT INTO insole_features VALUES( ?, ?, ?, ?, ?, ?)', params)
    conn.commit()
    conn.close()


# In[69]:


def addInsoleFeatures5(db_file, person,step, feature1, feature2, feature3, feature4, feature5):
    conn= create_connection(db_file)
    params= (person,step, feature1, feature2, feature3, feature4, feature5)
    conn.execute('INSERT INTO insole_features VALUES( ?, ?, ?, ?, ?, ?, ?)', params)
    conn.commit()
    conn.close()


# In[70]:


def addInsoleFeatures9(db_file, person,step, feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9):
    conn= create_connection(db_file)
    params= (person,step, feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9)
    conn.execute('INSERT INTO insole_features VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', params)
    conn.commit()
    conn.close()


# In[71]:


def addInsoleFeatures10(db_file, person,step, feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10):
    conn= create_connection(db_file)
    params= (person,step, feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10)
    conn.execute('INSERT INTO insole_features VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', params)
    conn.commit()
    conn.close()


# get the stored features

# In[72]:


# returns a list of the features for one person
def getPersonsStepFeatures1(db_file, person, step):
    verbindung = create_connection(db_file)
    zeiger = verbindung.cursor()
    zeiger.execute('SELECT * FROM insole_features WHERE person = ? AND step = ?', [person, step])
    inhalt = zeiger.fetchall()
    liste= []
    for vector in inhalt:
    

        #print(tupel[1])
        features= []
        
        #features.append(vector[1])
        features.append(vector[2])
        liste.append(features)
        
    verbindung.close()
    return liste


# In[73]:


# returns a list of the features for one person
def getPersonsStepFeatures2(db_file, person, step):
    verbindung = create_connection(db_file)
    zeiger = verbindung.cursor()
    zeiger.execute('SELECT * FROM insole_features WHERE person = ? AND step = ?', [person, step])
    inhalt = zeiger.fetchall()
    liste= []
    for vector in inhalt:
    

        #print(tupel[1])
        features= []
        
        #features.append(vector[1])
        features.append(vector[2])
        features.append(vector[3])
        #features.append(vector[4])
        #features.append(vector[5])
        #features.append(vector[6])
        #features.append(vector[7])
        liste.append(features)
        
    verbindung.close()
    return liste


# In[74]:


# returns a list of the features for one person
def getPersonsStepFeatures3(db_file, person, step):
    verbindung = create_connection(db_file)
    zeiger = verbindung.cursor()
    zeiger.execute('SELECT * FROM insole_features WHERE person = ? AND step = ?', [person, step])
    inhalt = zeiger.fetchall()
    liste= []
    for vector in inhalt:
    

        #print(tupel[1])
        features= []
        
        #features.append(vector[1])
        features.append(vector[2])
        features.append(vector[3])
        features.append(vector[4])
        #features.append(vector[5])
        #features.append(vector[6])
        #features.append(vector[7])
        liste.append(features)
        
    verbindung.close()
    return liste


# In[75]:


# returns a list of the features for one person
def getPersonsStepFeatures4(db_file, person, step):
    verbindung = create_connection(db_file)
    zeiger = verbindung.cursor()
    zeiger.execute('SELECT * FROM insole_features WHERE person = ? AND step = ?', [person, step])
    inhalt = zeiger.fetchall()
    liste= []
    for vector in inhalt:
    

        #print(tupel[1])
        features= []
        
        #features.append(vector[1])
        features.append(vector[2])
        features.append(vector[3])
        features.append(vector[4])
        features.append(vector[5])
        #features.append(vector[7])
        liste.append(features)
        
    verbindung.close()
    return liste


# In[76]:


# returns a list of the features for one person
def getPersonsStepFeatures5(db_file, person, step):
    verbindung = create_connection(db_file)
    zeiger = verbindung.cursor()
    zeiger.execute('SELECT * FROM insole_features WHERE person = ? AND step = ?', [person, step])
    inhalt = zeiger.fetchall()
    liste= []
    for vector in inhalt:
    

        #print(tupel[1])
        features= []
        
        #features.append(vector[1])
        features.append(vector[2])
        features.append(vector[3])
        features.append(vector[4])
        features.append(vector[5])
        features.append(vector[6])
        #features.append(vector[7])
        liste.append(features)
        
    verbindung.close()
    return liste


# In[77]:


# returns a list of the features for one person
def getPersonsStepFeatures9(db_file, person, step):
    verbindung = create_connection(db_file)
    zeiger = verbindung.cursor()
    zeiger.execute('SELECT * FROM insole_features WHERE person = ? AND step = ?', [person, step])
    inhalt = zeiger.fetchall()
    liste= []
    for vector in inhalt:
    

        #print(tupel[1])
        features= []
        
        #features.append(vector[1])
        features.append(vector[2])
        features.append(vector[3])
        features.append(vector[4])
        features.append(vector[5])
        features.append(vector[6])
        features.append(vector[7])
        features.append(vector[8])
        features.append(vector[9])
        features.append(vector[10])
        liste.append(features)
        
    verbindung.close()
    return liste


# In[78]:


# returns a list of the features for one person
def getPersonsStepFeatures10(db_file, person, step):
    verbindung = create_connection(db_file)
    zeiger = verbindung.cursor()
    zeiger.execute('SELECT * FROM insole_features WHERE person = ? AND step = ?', [person, step])
    inhalt = zeiger.fetchall()
    liste= []
    for vector in inhalt:
    

        #print(tupel[1])
        features= []
        
        #features.append(vector[1])
        features.append(vector[2])
        features.append(vector[3])
        features.append(vector[4])
        features.append(vector[5])
        features.append(vector[6])
        features.append(vector[7])
        features.append(vector[8])
        features.append(vector[9])
        features.append(vector[10])
        features.append(vector[11])
        liste.append(features)
        
    verbindung.close()
    return liste


# add features of one person

# In[79]:


def getStepsOfPerson(db_file, person):
    
    verbindung = create_connection(db_file)
    zeiger = verbindung.cursor()
    zeiger.execute('SELECT * FROM insole_features WHERE person = ?', [person])
    inhalt = zeiger.fetchall()
    
    steps=set()
    for vector in inhalt:
    

        steps.add(vector[1])
        
        
    verbindung.close()
    return steps
    


# In[80]:


def getStepList(db_file, person, numFeatures):
    steps=getStepsOfPerson(db_file, person)
    stepFeaturesPersDB= []
    for step in steps:
        if numFeatures==1:
            stepFeaturesPersDB.append(getPersonsStepFeatures1(db_file, person, step))
        elif numFeatures==2:
            stepFeaturesPersDB.append(getPersonsStepFeatures2(db_file, person, step))
        elif numFeatures==3:
            stepFeaturesPersDB.append(getPersonsStepFeatures3(db_file, person, step))
        elif numFeatures==4:
            stepFeaturesPersDB.append(getPersonsStepFeatures4(db_file, person, step))
        elif numFeatures==5:
            stepFeaturesPersDB.append(getPersonsStepFeatures5(db_file, person, step))
        elif numFeatures==9:
            stepFeaturesPersDB.append(getPersonsStepFeatures9(db_file, person, step))
        elif numFeatures==10:
            stepFeaturesPersDB.append(getPersonsStepFeatures10(db_file, person, step))
    return stepFeaturesPersDB


# In[81]:


def addFeatures(db_file, listOfPersons, listOfStepFeatures, numFeatures):
    index=0
    for person in listOfPersons:
        print(person)
        st=1
        for step in listOfStepFeatures[index]:
            print(step)
            print(len(step))
            for features in step:
                print(features)
                print(len(features))
                if numFeatures==1:
                    addInsoleFeatures1(db_file, person, st, features[0])
                elif numFeatures==2:
                    addInsoleFeatures2(db_file, person, st, features[0], features[1])
                elif numFeatures==3:
                    addInsoleFeatures3(db_file, person, st, features[0], features[1], features[2])
                elif numFeatures==4:
                    addInsoleFeatures4(db_file, person, st, features[0], features[1], features[2], features[3])
                elif numFeatures==5:
                    addInsoleFeatures5(db_file, person, st, features[0], features[1], features[2], features[3], features[4])
                elif numFeatures==9:
                    addInsoleFeatures9(db_file, person, st, features[0], features[1], features[2], features[3], features[4], features[5], features[6], features[7], features[8])
                elif numFeatures==10:
                    addInsoleFeatures10(db_file, person, st, features[0], features[1], features[2], features[3], features[4], features[5], features[6], features[7], features[8], features[9])
            st+=1
        index+=1
    

