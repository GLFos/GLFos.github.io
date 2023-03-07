#%

import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn import linear_model
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


#Extracting the Data from the CSV File
data = pd.read_csv("C:\\Users\\GLFos\\Documents\\ML Fraud CSV's\\creditcard.csv")


#Cleaning and Preprocessing the Data
data = data.dropna()
data = data.drop_duplicates()
fraud = data.loc[data['Class'] == 1]
normal = data.loc[data['Class'] == 0]

#Exploring the Data
#print(data.describe())
sns.countplot(x='Class', data=data)

#Feature Engineering
X = data.iloc[:,:-1]
y = data['Class']

#Scale Data
scaler = StandardScaler()
X = scaler.fit_transform(X)

#Training the Logistic Regression Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 42)
clf = linear_model.LogisticRegression(C=1e5, fit_intercept=False, max_iter=10000)
clf.fit(X_train, y_train)


#Forming and Fitting the Pipeline
pipeline = Pipeline([("scaler", StandardScaler()), ("model", linear_model.LogisticRegression(C=1e5, fit_intercept=False, max_iter=10000))])
pipeline.fit(X_train, y_train)

#Predictions of Test Data
y_pred = pipeline.predict(X_test)

#Hyperparameter Tuning
param_grid = {"model__fit_intercept": [True,False]}
gridsearch = GridSearchCV(pipeline, param_grid = param_grid, scoring = "neg_mean_squared_error", cv = 5)
gridsearch.fit(X_train, y_train)

#Evaluate the model's performance post Tuning
print("Accuracy: {:.2f}".format(accuracy_score(y_test, y_pred)))
print("Precision: {:.2f}".format(precision_score(y_test, y_pred)))
print("Recall: {:.2f}".format(recall_score(y_test, y_pred)))
print("F1 Score: {:.2f}".format(f1_score(y_test, y_pred)))

print("Best parameters: ", gridsearch.best_params_)
print("Best score: ", -gridsearch.best_score_)