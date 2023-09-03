import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(20, 2))
print(df.sort_index(ascending=False))  # 降順

print(df.sort_values(by=1))  # key(カラム名)が1の昇順でソート
print(df.sort_values(by=1, ascending=False))  # keyが１の降順でソート
