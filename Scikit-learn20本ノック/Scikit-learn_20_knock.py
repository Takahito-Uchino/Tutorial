import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob
import sklearn.preprocessing as sp
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, r2_score, mean_squared_error
from sklearn.neighbors import KNeighborsClassifier

#df = pd.read_csv('/Users/takahitouchino/Project/Scikit-learn20本ノック/data.csv', encoding = 'utf-8')
#print(df.head(5))
#print(df.isnull().sum())
#df = df.dropna(axis = 0)
#print(df)
#print(df['Age'].describe())
#print(np.median(df['Age']))
#print(df[['Age']].fillna(0))
#print(df[['Age']].fillna(int(df['Age'].mean())))
#print(df[['Age']].fillna(df['Age'].median()))
#age_mean = df['Age'].mean()
#age_std = df['Age'].std()
#age_nan = df['Age'].isnull().sum()
#rand = np.random.randint(age_mean - age_std, age_mean + age_std, age_nan)
#print(a)
#plt.hist(df['Age'].dropna().astype(int), bins = 70)
#plt.show()
#age_append = df['Age'].fillna(np.random.randint(age_mean - age_std, age_mean + age_std))
#print(age_append)
#plt.hist(age_append, bins = 70)
#plt.show()
#df.loc[df['Age'].isnull(), 'Age'] = rand
#print(df['Age'].isnull().sum())
#plt.hist(df['Age'], bins = 70)
#plt.show()
#df['Sex'] = df['Sex'].fillna(method = 'ffill')
#print(df['Sex'])
#df['Sex'] = pd.get_dummies(df['Sex']).drop('male', axis = 1)
#print(df['Sex'])
#age_minmax_scale = sp.minmax_scale(df['Age'])
#print(age_minmax_scale)
#plt.plot(age_minmax_scale)
#plt.show()
#age_scale = sp.scale(df['Age'])
#print(age_scale)
#plt.plot(age_scale)
#plt.show()
#print(age_scale.mean())
#df_wine = pd.read_csv('/Users/takahitouchino/Project/Scikit-learn20本ノック/wine.csv', encoding = 'utf-8')
#print(df_wine.head())
#print(df_wine.columns)
"""
dfs = sp.scale(df_wine[['Alcohol'], ['Malic acid'], ['Ash'], ['Alcalinity of ash'],
       ['Magnesium'], ['Total phenols'], ['Flavanoids'], ['Nonflavanoid phenols'],
       ['Proanthocyanins'], ['Color intensity'], ['Hue'],
       ['OD280/OD315 of diluted wines'], ['Proline']])
print(dfs)
"""
#_dfs = sp.scale(df_wine.iloc[:, 1:])
#print(_dfs)
#fs = pd.DataFrame(_dfs, columns = df_wine.columns[1:])
#print(dfs)
#pca = PCA()
#x = pca.fit_transform(dfs)
#feature = pd.DataFrame(x, columns = ['PC{}'.format(i + 1) for i in range(len(dfs.columns))])
#print(feature.head())
#print(feature.shape)
"""
plt.figure(figsize = (6, 6))
plt.scatter(feature['PC1'],feature['PC2'], alpha = 0.8, c = df_wine['class'])
plt.grid()
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()
X = feature.iloc[:, :2]
y = df_wine.iloc[:, 0]
X_train, X_test, y_train, y_test = (train_test_split(X, y, test_size = 0.2, random_state = 3))
print(X_train)
print(X_test)
print(y_train)
print(y_test)
"""
"""
lr = LogisticRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
#print(y_pred)
#print(accuracy_score(y_true = y_test, y_pred = y_pred))
"""
"""
knc = KNeighborsClassifier(n_neighbors = 40)
knc.fit(X_train, y_train)
y_pred = knc.predict(X_test)
print(accuracy_score(y_true = y_test, y_pred = y_pred))
"""
df_slump = pd.read_csv('/Users/takahitouchino/Project/Scikit-learn20本ノック/slump.csv', encoding = 'utf-8')
#print(df_slump.head())
X = df_slump.iloc[:, :7]
Y = df_slump.iloc[:, -1]
X_train, X_test, Y_train, Y_test = (train_test_split(X, Y, test_size = 0.4, random_state = 0))
regressor = LinearRegression()
regressor.fit(X_train, Y_train)
Y_pred = regressor.predict(X_test)
print(r2_score(Y_test, Y_pred))
print(np.sqrt(mean_squared_error(Y_test, Y_pred)))