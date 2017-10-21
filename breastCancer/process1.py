import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
def preProcessData():
    columnName = list("ABCDEFGHIJK")
    data = pd.read_csv("D:/work_space/ML_practice/data/breast-cancer-wisconsin.data", names=columnName)
    data = data.replace(to_replace='? ', value=np.nan)
    data = data.dropna(how='any')
    print(data.shape)
    return data, columnName

def crossValidation(data, columnNames):
    X_train, X_test, Y_train, Y_test = train_test_split(data[columnNames[1:10]], data[columnNames[10]], test_size=0.25, random_state=33)
    print(Y_test.value_counts())
    print(X_train.value_counts())

def add(a, b):
    print(a, b)

if __name__ == "__main__":
    #add(*(1, 2))
    crossValidation(*preProcessData())
