import pandas as pd

df = pd.DataFrame([[10, 20], [25, 50]], index=[
                  '１行', '２行'], columns=['１列', '２列'])

print(df.loc['１行', :])
print(df.loc[:, ['１列', '２列']])

# df.iloc[行, 列]
print(df.iloc[1:2])  # index指定が可能

print(df.iloc[:, -1])  # 負のインデックスを使い、末尾の要素から位置指定し２列目のすべての行を取得。
