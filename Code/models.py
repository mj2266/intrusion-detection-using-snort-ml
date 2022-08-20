from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB,MultinomialNB
import numpy as np




## function to calculate false alarm rate
def calculate_flr(y_test,y_pred) :

    '''False Alarm Rate'''

    cm=confusion_matrix(y_test,y_pred)
    tn, fp, fn, tp = cm.ravel()
    return (fp+fn)/tp




## Following functions train various ML algorithms on train data and output accuracy for the test data 


def rfc(X_train,X_test,y_train,y_test) :

    '''Random Forest Classifier'''

    model=RandomForestClassifier(max_depth=20)
    model.fit(X_train, y_train)
    y_pred= model.predict(X_test)
    #print('Random Forest Classifier: ')
    #print(confusion_matrix(y_test, y_pred))
    return accuracy_score(y_test,y_pred),calculate_flr(y_test,y_pred)





def abc(X_train,X_test,y_train,y_test) :

    '''Ada Boost Classifier'''

    model=AdaBoostClassifier()
    model.fit(X_train, y_train)
    y_pred= model.predict(X_test)
    #print('Adaboost Classifier: ')
    #print(confusion_matrix(y_test, y_pred))
    return accuracy_score(y_test,y_pred),calculate_flr(y_test,y_pred)





def mlp(X_train,X_test,y_train,y_test) :

    '''MLP Classifier'''

    model=MLPClassifier()
    model.fit(X_train, y_train)
    y_pred= model.predict(X_test)
    #print('MLP Classifier: ')
    #print(confusion_matrix(y_test, y_pred))
    return accuracy_score(y_test,y_pred),calculate_flr(y_test,y_pred)





def GBclassifier(X_train,X_test,y_train,y_test) :

    '''Gradient Boost Classifier'''

    model=GradientBoostingClassifier()
    model.fit(X_train, y_train)
    y_pred= model.predict(X_test)
    #print('Gradient Boosting Classifier: ')
    #print(confusion_matrix(y_test, y_pred))
    return accuracy_score(y_test,y_pred),calculate_flr(y_test,y_pred)





def lr(X_train,X_test,y_train,y_test,max_iter=100) :

    '''Logistic Regressor'''

    model=LogisticRegression(max_iter=max_iter)
    model.fit(X_train, y_train)
    y_pred= model.predict(X_test)
    #print('Logistic Regression')
    #print(confusion_matrix(y_test, y_pred))
    return accuracy_score(y_test,y_pred),calculate_flr(y_test,y_pred)





def SGD(X_train,X_test,y_train,y_test) :

    '''SGD Classifier'''

    model=SGDClassifier()
    model.fit(X_train, y_train)
    y_pred= model.predict(X_test)
    #print('SGD Classifier:')
    #print(confusion_matrix(y_test, y_pred))
    return accuracy_score(y_test,y_pred),calculate_flr(y_test,y_pred)





def DT(X_train,X_test,y_train,y_test) :

    '''DecisionTree Classifier'''

    model=DecisionTreeClassifier()
    model.fit(X_train, y_train)
    y_pred= model.predict(X_test)
    #print('DT Classifier:')
    #print(confusion_matrix(y_test, y_pred))
    return accuracy_score(y_test,y_pred),calculate_flr(y_test,y_pred)





def KNN(X_train,X_test,y_train,y_test) :

    '''KNN Classifier'''

    model=KNeighborsClassifier()
    model.fit(X_train, y_train)
    y_pred= model.predict(X_test)
    #print('KNN Classifier:')
    #print(confusion_matrix(y_test, y_pred))
    return accuracy_score(y_test,y_pred),calculate_flr(y_test,y_pred)





def Histclassifier(X_train,X_test,y_train,y_test) :

    '''Histogram Based Gradient'''

    model=HistGradientBoostingClassifier()
    model.fit(X_train, y_train)
    y_pred= model.predict(X_test)
    #print('Hist GB Classifier:')
    #print(confusion_matrix(y_test, y_pred))
    return accuracy_score(y_test,y_pred),calculate_flr(y_test,y_pred)





def GNB(X_train,X_test,y_train,y_test) :

    '''Gaussian Naive Bias'''

    model=GaussianNB()
    model.fit(X_train, y_train)
    y_pred= model.predict(X_test)
    #print('Gaussian Naive Bias:')
    #print(confusion_matrix(y_test, y_pred))
    return accuracy_score(y_test,y_pred),calculate_flr(y_test,y_pred)




def MNB(X_train,X_test,y_train,y_test) :

    '''Multinomial Naive Bias'''

    model=MultinomialNB()
    model.fit(X_train, y_train)
    y_pred= model.predict(X_test)
    #print('Multinomial Naive Bias:')
    #print(confusion_matrix(y_test, y_pred))
    return accuracy_score(y_test,y_pred),calculate_flr(y_test,y_pred)