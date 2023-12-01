#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import roc_auc_score, balanced_accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib
import HelpFunctions
import matplotlib.pyplot as plt
import numpy as np
matplotlib.rcParams['mathtext.fontset'] = 'custom'
matplotlib.rcParams['mathtext.rm'] = 'Bitstream Vera Sans'
matplotlib.rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'
matplotlib.rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'
sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
matplotlib.rcParams['font.size']= 24


# In[ ]:


def extendTrainAndTestSet(stepFeaturesPersDB, label, testEnd, trainEnd, trainFeatures, trainLabels, testFeatures, testLabels):
    trainPUnflat= stepFeaturesPersDB[0:testEnd]
    #trainP1=[]
    for l in trainPUnflat:
        #trainP1.append([element for sublist in l for element in sublist])
        trainFeatures.append([element for sublist in l for element in sublist])
        
        trainLabels.append(label)
    

    testPUnflat= stepFeaturesPersDB[testEnd:trainEnd]
    #testP1=[]
    for l in testPUnflat:
        #testP1.append([element for sublist in l for element in sublist])
        testFeatures.append([element for sublist in l for element in sublist])
        testLabels.append(label)
    
    return trainFeatures, trainLabels, testFeatures, testLabels


# In[ ]:


def runClassifiers(trainFeatures, testFeatures, trainLabels, testLabels, numOfFeatures,smoothFactor,steps, save_results_to, xlabels,ylabels):
    # first, initialize the classificators
    tree= DecisionTreeClassifier(random_state=42) # using the random state for reproducibility
    forest= RandomForestClassifier(random_state=42)
    knn= KNeighborsClassifier()
    svm= SVC(random_state=42)
    xboost= XGBClassifier(random_state=42)

    # X = df_train.drop(['y'] , axis=1)
    # y = df_train['y']

    # X_test = df_test.drop(['y'] , axis = 1)
    # y_test = df_test['y']
    acc = []
    other_accuracy=[]
    mo = []
    models= [tree, forest, knn, svm, xboost]

    #X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2 , random_state=42)
    X_train= trainFeatures
    X_test= testFeatures
    y_train= trainLabels
    y_test= testLabels
    HelpFunctions.replace_none_with_zero(X_train)
    HelpFunctions.replace_inf_with_zero(X_train)
    #round_float_to_int(X_train)
    #print(X_train)
    HelpFunctions.replace_none_with_zero(X_test)
    HelpFunctions.replace_inf_with_zero(X_test)
    #round_float_to_int(X_test)
    #print(X_test)

    print(X_train)
    print(y_train)

    print(len(X_train))
    print(len(y_train))

    for model in models:
        model.fit(X_train,y_train) # fit the model
        y_pred= model.predict(X_test) # then predict on the test set
        accuracy= accuracy_score(y_test, y_pred) # this gives us how often the algorithm predicted correctly
        other_acc= balanced_accuracy_score(y_test,y_pred)
        other_accuracy.append(other_accuracy)
        acc.append(accuracy)
        clf_report= classification_report(y_test, y_pred) # with the report, we have a bigger picture, with precision and recall for each class
        print(f"The accuracy of model {type(model).__name__} is {accuracy:.3f}")
        print(f"The \"other accuracy\" of model {type(model).__name__} is {other_acc:.3f}")
        mo.append(type(model).__name__)
        print(clf_report)
        # plot confusion Matrix
        
        cm = confusion_matrix(y_test, y_pred)
        cmn = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

        # Create a custom color palette for the heatmap with a single color
        cmap = sns.color_palette("Blues", as_cmap=True)

        fig, ax = plt.subplots(figsize=(14, 14))

        # Anpassungen für bessere Lesbarkeit und einheitliche Intensität
        sns.heatmap(cmn, annot=True, fmt='.2f', cmap=cmap, linewidths=0.5, square=True, xticklabels=xlabels,yticklabels=ylabels,annot_kws={"fontsize": 16, "color": 'black'})  # Verwendung der Schriftfarbe 'black'

        # Customize labels und Farben
        ax.set_xlabel('Predicted', fontsize=18)
        ax.set_ylabel('Actual', fontsize=18)
        ax.set_title(f'{type(model).__name__} Confusion Matrix {numOfFeatures} Features', fontsize=24, pad=20)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)

        # Add colorbar
        cbar = ax.collections[0].colorbar
        cbar.set_label('Normalized Values', fontsize=16)

        # Save the figure and display it
        plt.savefig(save_results_to + f'{type(model).__name__}_Confusion Matrix_{numOfFeatures}Features_SmoothFactor{smoothFactor}_Steps{steps}.pdf', dpi=300, bbox_inches='tight')
        plt.show()

        print("\n")

    print('------------------------------------------------------------------------------------')

