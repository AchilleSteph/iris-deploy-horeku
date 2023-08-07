
# main is a class containing prediction method

# load librairies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from joblib import dump
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# load data iris
iris = load_iris()
iris

# target and predictive variables
X = iris.data
y = iris.target
X.shape, y.shape

# training session
log_reg = LogisticRegression(max_iter=800)
log_reg.fit(X, y)

def iris_prediction(sl, sw, pl, pw):
    new_data = [[sl, sw, pl, pw]]
    return iris.target_names[ log_reg.predict(new_data)[0] ]


