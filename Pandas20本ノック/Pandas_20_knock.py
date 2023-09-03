import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
    '/Users/uchinotakahito/Project/Pandas20本ノック/weather.csv', encoding='utf-8')
# print(df)
# print(df.head(3).append(df.tail(10)))
# print(df.columns)
# print(df.index)
df = df[['年月日', '平均気温(℃)', '最高気温(℃)', '最低気温(℃)', '降水量の合計(mm)', '最深積雪(cm)',
         '平均雲量(10分比)', '平均蒸気圧(hPa)', '平均風速(m/s)', '日照時間(時間)']][1:]
# print(df)
# print(df.dtypes)
# print(df.shape)
# print(df.columns)
# print(df.index)
# print(df.iloc[4: 10, 2: 6])
# print(df.loc[5: 10, '最高気温(℃)': '最深積雪(cm)'])
df_people = pd.read_csv(
    '/Users/uchinotakahito/Project/Pandas20本ノック/people.csv', encoding='utf-8')
# print(df_people)
# print(df_people[df_people['nationality'] == 'America'])
# print(df_people.query('nationality == "America"'))
# print(df_people[df_people['nationality'].isin(['America'])])
# print(df_people[(df_people['age'] >= 20) & (df_people['age'] < 30)])
# print(df_people.query('age >= 20 & age < 30'))
# print(df_people['nationality'].unique())
# print(df_people.drop_duplicates(subset='nationality'))
df.columns = ['年月日', '平均気温', '最高気温', '最低気温', '降水量の合計', '最深積雪',
              '平均雲量', '平均蒸気圧', '平均風速', '日照時間']
# df = df.rename(columns={'平均気温(℃)': '平均気温', '最高気温(℃)': '最高気温', '最低気温(℃)': '最低気温', '降水量の合計(mm)': '降水量の合計', '最深積雪(cm)': '最深積雪',
#                        '平均雲量(10分比)': '平均雲量', '平均蒸気圧(hPa)': '平均蒸気圧', '平均風速(m/s)': '平均風速', '日照時間(時間)': '日照時間'})
# print(df)
# print(df.sort_values('最高気温', ascending=False))
# print(df_people.dtypes)
# print(pd.get_dummies(df_people, columns=['nationality']))
# print(df.isnull())
# print(df.isnull().sum())
# df = df.fillna(0)
# print(df)
# df = df[['年月日', '平均気温', '最高気温', '最低気温',
#         '降水量の合計', '平均風速', '日照時間']]
df = df.dropna(axis=1)
# print(df)
df_iris = pd.read_csv(
    '/Users/uchinotakahito/Project/Pandas20本ノック/iris.csv', encoding='utf-8')
# print(iris)
# print(iris['Class'].value_counts())
#     sepal-length  sepal-width  petal-length  petal-width
# print(df_iris.groupby('Class').mean())
# print(df.mean())
# print(df.median())
# print(df.std())
# print(df.max())
# print(df.min())
# print(df.describe())
"""x = df['年月日'].head(50)
y1 = df['平均気温'].head(50)
y2 = df['最高気温'].head(50)
y3 = df['最低気温'].head(50)
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show()"""
# df[: 50].plot(x='年月日', y=['平均気温', '最高気温', '最低気温'])
# plt.show()
# x = np.array(df['平均気温'], df['降水量の合計'])
# print(np.corrcoef(x, df['日照時間']))
# print(df[['平均気温', '降水量の合計', '日照時間']].corr())
# print(df)
df.fillna(0).to_csv(
    '/Users/uchinotakahito/Project/Pandas20本ノック/export.csv', index=False)
