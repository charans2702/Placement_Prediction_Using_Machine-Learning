import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
df = pd.read_csv('data2.csv')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df.fillna(0,inplace=True)
x=df.drop(['StudentId','PlacementStatus'],axis=1)
y = df['PlacementStatus']
le = preprocessing.LabelEncoder()
x['Internship'] = le.fit_transform(x['Internship'])
x['Hackathon'] = le.fit_transform(x['Hackathon'])
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 100)
classify= RandomForestClassifier(n_estimators= 100, criterion="entropy")
classify.fit(x_train, y_train)
ypred=classify.predict(x_test)
from sklearn.metrics import accuracy_score
a=accuracy_score(ypred,y_test)
print(a)
pickle.dump(classify, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
print(classify.predict([[8,1,3,2,9,4.8,0,1,71,87,0]]))
