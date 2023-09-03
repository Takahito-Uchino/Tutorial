import numpy as np
import pandas as pd

s1 = pd.Series([1, 3, 5, 7])
print(s1)

df1 = pd.DataFrame({
    '名前': ['古里', 'Sleek', '内野'],
    '役割': ['CEO', 'CTO', '生徒'],
    '身長': [180, 175, 170]
})
print(df1)

data1 = pd.read_csv('/Users/uchinotakahito/Project/NumPy_Pands_Matplotlib_Scikit-learn_Tutorial/Pandas_Tutorial/sns_data.csv',
                    encoding='utf-8')
print(data1)
data1.columns = ['user_id', 'follow', 'follower', 'like']
print(data1)
# data1.to_csv('/Users/uchinotakahito/Project/NumPy_Pands_Matplotlib_Scikit-learn_Tutorial/Pandas_Tutorial/sns_data_english.csv',
#             index=False, encoding='utf-8')

d1 = {'data1': ['a', 'b', 'c', 'd', 'c', 'a'], 'data2': range(6)}
d1 = pd.DataFrame(d1)
print(d1)

# d1.to_csv('/Users/uchinotakahito/Project/NumPy_Pands_Matplotlib_Scikit-learn_Tutorial/Pandas_Tutorial/d1_csv.csv',
#          encoding='utf-8')

# d1.to_excel('/Users/uchinotakahito/Project/NumPy_Pands_Matplotlib_Scikit-learn_Tutorial/Pandas_Tutorial/d1_excel.xlsx',
#            encoding='utf-8')

d2 = pd.read_csv('/Users/uchinotakahito/Project/NumPy_Pands_Matplotlib_Scikit-learn_Tutorial/Pandas_Tutorial/d1_csv.csv',
                 encoding='utf-8')
print(d2)

d3 = pd.read_excel(
    '/Users/uchinotakahito/Project/NumPy_Pands_Matplotlib_Scikit-learn_Tutorial/Pandas_Tutorial/d1_excel.xlsx')
print(d3)

d3['data3'] = 0
print(d3)

d3 = d3.append({'Unnamed: 0': 6, 'data1': 'c',
                'data2': 6, 'data3': 0}, ignore_index=True)
print(d3)
