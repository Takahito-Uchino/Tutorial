import numpy as np
import pandas as pd

df = pd.DataFrame({'int': [1, np.nan, np.nan, 32],
                   'str': ['python', 'ai', np.nan, np.nan],
                   'flt': [5.5, 4.2, -1.2, np.nan]})
print(df)

# df成分に対してNaNの地位をTrueとしたBoolの値のデータフレームを返す
print(df.isnull())
print(df.notnull())  # notnull()を使うと、TrueとFalseが逆の処理になる

# 'int'列にNaNがある行の削除
print(df.dropna(subset=['int']))

# NaNがある行を全て削除
print(df.dropna())

# NaNを全て0に置換する
print(df.fillna(0))
# 第１引数にmethod='ffill' 第２引数にlimtit=数字とすることで指定した数字までは前のデータを使ってNaNを埋めることができる

df2 = pd.DataFrame({'int': [1, np.nan, np.nan, 32],
                    'str': ['python', 'ai', np.nan, np.nan],
                    'flt': [5.5, 4.2, -1.2, np.nan]})
# int列だけ0で補完
print(df2.fillna({'int': 0}))  # 特定の列に対しては辞書型を用いる
# 列ごとに異なる値を使いたい場合は複数のキーを渡す
print(df2.fillna({'int': 0, 'str': 'ai'}))
# 特定の列（例えばflt)を削除
print(df2.drop(labels='flt', axis=1))
# 複数の列を削除
print(df2.drop(labels=['flt', 'str'], axis=1))
# indexを指定すると行を消せる
print(df2.drop(index=1, axis=0))
# 元のデータに反映して削除するにはinplaceオプションにTrueを渡す
df2.drop(labels='flt', axis=1, inplace=True)
print(df2)
