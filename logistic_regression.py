import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.LabelEncoder # https://qiita.com/uratatsu/items/8bedbf91e22f90b6e64b

def change_nominal_scale(se, a, b):
    for i in range(len(se)):
        print(se[i])
        if se[i] == a:
            se[i] = 0
        else:
            se[i] = 1
    return se

train = pd.read_csv('train.csv')
x_train = train.loc[:, 'cat0':'cont10']
y_train = train['target']

test = pd.read_csv('test.csv', index_col=0)
x_test = test.loc[:, 'cat0':'cont10']

a = [['A','B'],['I','F'],['A','C'],['A','B'],['E','F'],['BI','AB'],['A','C'],['AH','E'],['BM','AE'],['A','E'],['DJ','HK'],['A','B'],['A','B'],['A','B'],['A','B'],['B','D'],['D','B'],['D','B'],['B','D']]
for i in range(0,19):
    x_train['cat%d' % i] = change_nominal_scale(x_train['cat%d' % i], a[i][0], a[i][1])
    x_test['cat%d' % i] = change_nominal_scale(x_test['cat%d' % i], a[i][0], a[i][1])

print(x_train)

# model = LogisticRegression()
# model.fit(x_train, y_train)

# y_pred = model.predict(x_test)

# df = pd.DataFrame(index = test['id'])
# df['target'] = y_pred

# df.to_csv('submission_lr.csv')