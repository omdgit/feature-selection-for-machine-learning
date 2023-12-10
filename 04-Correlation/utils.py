import pandas as pd 

def increase(X):
    X['income'] = X['income'] * 1.1
    X['age'] = X['age'] + 1
    return X