# -*- coding: utf-8 -*-
"""ai

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xxO-rSrw7Pz9c70SEdQnWRB3-UaBrUoi

## **Chance of Admission for Higher Studies**
Predict the chances of admission of a student to a Graduate program based on:

GRE Scores (290 to 340)

TOEFL Scores (92 to 120)

University Rating (1 to 5)

Statement of Purpose (1 to 5)

Letter of Recommendation Strength (1 to 5)

Undergraduate CGPA (6.8 to 9.92)

Research Experience (0 or 1)

Chance of Admit (0.34 to 0.97)
"""

# Step 1 : import library
import pandas as pd

# Step 2 : import data
admission = pd.read_csv('https://github.com/ybifoundation/Dataset/raw/main/Admission%20Chance.csv')

admission.head()

admission.info()

admission.describe()

# Step 3 : define target (y) and features (X)
admission.columns

y = admission['Chance of Admit ']

X = admission.drop(['Serial No','Chance of Admit '],axis=1)

# Step 4 : train test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, train_size=0.7, random_state=2529)

# check shape of train and test sample
X_train.shape, X_test.shape, y_train.shape, y_test.shape

# Step 5 : select model
from sklearn.linear_model import LinearRegression
model = LinearRegression()

# Step 6 : train or fit model
model.fit(X_train,y_train)

model.intercept_

model.coef_

# Step 7 : predict model
y_pred = model.predict(X_test)

y_pred

# Step 8 : model accuracy
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error

mean_absolute_error(y_test,y_pred)

mean_absolute_percentage_error(y_test,y_pred)

mean_squared_error(y_test,y_pred)