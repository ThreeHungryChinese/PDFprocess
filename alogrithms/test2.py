from sklearn import linear_model
import os
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import sys

class Admission_Predictor:
    def __init__(self):
        path = '/Users/peiqingxuan/Desktop/'
        os.chdir(path)
        self.data = pd.read_csv("Admission_Predict.csv")
    def model_train_and_predict(self, data_l):
        cols = self.data.columns
        features = cols[1:-1]
        target = cols[-1]
        X = self.data[features]
        y = self.data['Chance of Admit ']
        ## datal stands for new line of data, i really can not fucking think what to name this right now
        ## kz 2019 10 14 00:01
        Xnew = np.array(data_l).reshape(1,-1)

        # Linear Regression
        model = linear_model.LinearRegression()
        model.fit(X,y)
        ynew = model.predict(Xnew)

        # Decision Tree Regression
        model2 = DecisionTreeRegressor()
        model2.fit(X,y)
        ynew2 = model2.predict(Xnew)

        # Ridge Regression
        model3 = linear_model.Ridge()
        model3.fit(X,y)
        ynew3 = model3.predict(Xnew)

        # Lasso Linear Model
        model4 = linear_model.Lasso()
        model4.fit(X,y)
        ynew4 = model4.predict(Xnew)

        # Least Angle Lasso Regression
        model5 = linear_model.LassoLars()
        model5.fit(X,y)
        ynew5 = model5.predict(Xnew)

        # Bayesian Regression
        model6 = linear_model.BayesianRidge()
        model6.fit(X,y)
        ynew6 = model6.predict(Xnew)
        #print(ynew,ynew2,ynew3,ynew4,ynew5,ynew6)

        return ynew[0],ynew2[0],ynew3[0],ynew4[0],ynew5[0],ynew6[0]


def main(l):

    for i in range(len(l)):
        l[i] = float(l[i])
    adpred = Admission_Predictor()
    a,b,c,d,e,f = adpred.model_train_and_predict(l)
    return a,b,c,d,e,f


