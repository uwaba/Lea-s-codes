old data short: 
'BAN-System\Insole\ML_Classifiers\DataSteps5min'
- 6,8,11 nicht genug Daten 

new data short: 
'BAN-System\Insole\ML_Classifiers\DataSteps1min'
- 23,28 nicht genug Daten
- 110 Schritte pro Person (Aufteilung: test set bis index 80, train set bis index 110)

longer data:
'BAN-System\Insole\ML_Classifiers\DataSteps'
- 500 Schritte pro Person (Aufteilung: test set bis index 350 (70%), train set bis index 500)
'.//Database//new//insole_Smooth0Features9_l.db'
'.//Database//new//insole_Smooth0Features4_l.db'

original path for data: 
'BAN-System\Insole\V4_Christian\V2_TinyPico\Datenerhebung'


use 'jupyter nbconvert --to script Processing.ipynb' to convert jupyter notebook to script

## Main_Write
- includes entire process to setup a database 
- adjust smoothingFactor (for 0 the data is not changed)
- adjust the names of the folders in the urls
- adjust the url to the database (if the database does not exist yet use DatabaseSetup.py to create one)

## Main_Read
- includes entire process for reading data from an existing Database and classifying it
- adjust the names of the heatmap and the names to store the heatmaps depending on the number of features and the smoothing factor

## Processing 
- includes functions to process the steps

## Insole_Separation
- includes functions to extract specific parts of the insole 
- use the extractXParts function to split the insole into X parts

## FeatureExtraction
- includes functions to extract features

## MachineLearning
- includes functions to run Machine Learning Classifiers

## HelpFunctions
- includes functions to avoid NAN values

## DatabaseSetup
- to setup or delete a new database

## DatabaseManage
- includes functions to add/ remove or get data from the database

## MergeSteps
- includes function mergeSteps to merge the features of several steps to one (use the mean value) 
- includes fuinction addSteps to concatenate a number of randomly chosen (not necessarily following) steps to one list (the featurelist of one step includes then features of several steps--> e.g. data is not separated into single steps but into intervals of 5 steps) 
