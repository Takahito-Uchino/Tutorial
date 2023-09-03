import pandas as pd

data = pd.read_csv(
    'https://aiacademy.jp/dataset/sample_data.csv', encoding='cp932', skiprows=1)
# １行読み飛ばす
print(data)
print(type(data))
# <class 'pandas.core.frame.DataFrame'>
print(data.dtypes)
"""
エクセルの場合は下記のように使う。
.read_excel('任意のファイル名.xlsx', encoding='utf-8')
"""
