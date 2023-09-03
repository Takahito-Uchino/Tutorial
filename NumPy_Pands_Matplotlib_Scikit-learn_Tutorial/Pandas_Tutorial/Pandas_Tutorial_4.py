import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(20, 2))
print(df.head())  # 先頭から５件
print(df.tail())  # 末尾から５件

print(df.head().append(df.tail()))  # 先頭から５件と末尾から５件の計１０件を取得
print(df.head(3).append(df.tail(3)))  # 先頭から３件と末尾から３件の計６件を取得
