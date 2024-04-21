# Importing libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import shap
import warnings
import joblib


warnings.filterwarnings('ignore')


plt.style.use('ggplot')

df = pd.read_csv('/Users/mdfazil/Desktop/CollegeProject/CollegeProject/BackEnd/DataSet/diagnostic_values.csv')
df.drop(['id', 'Unnamed: 32'], axis = 1, inplace = True)
df['diagnosis'] = df['diagnosis'].apply(lambda val: 1 if val == 'M' else 0)

corr_matrix = df.corr().abs()

mask = np.triu(np.ones_like(corr_matrix, dtype = bool))
tri_df = corr_matrix.mask(mask)

to_drop = [x for x in tri_df.columns if any(tri_df[x] > 0.92)]

df = df.drop(to_drop, axis = 1)
print(df.columns)
print(f"The reduced dataframe has {df.shape[1]} columns.")

X = df.drop('diagnosis', axis = 1)
y = df['diagnosis']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 0)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

svc = SVC()
parameters = {
    'gamma' : [0.0001, 0.001, 0.01, 0.1],
    'C' : [0.01, 0.05, 0.5, 0.1, 1, 10, 15, 20]
}

grid_search = GridSearchCV(svc, parameters)
grid_search.fit(X_train, y_train)

svc = SVC(C = 10, gamma = 0.01)
svc.fit(X_train, y_train)

joblib.dump(svc, 'model2.pkl')
print("finished")