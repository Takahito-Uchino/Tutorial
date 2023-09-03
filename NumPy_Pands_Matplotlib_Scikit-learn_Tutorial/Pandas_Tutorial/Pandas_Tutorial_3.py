import pandas as pd

data = {
    '名前': ['田中', '山田', '高橋'],
    '役割': ['営業部長', '広報部', '技術責任者'],
    '身長': [178, 173, 169]
}

df = pd.DataFrame(data, columns=['名前', '役割', '身長'])
print(df)
# データフレーム生成時に対応するデータを持っていない場合、そのデータの列にはNaNが割り当てられる。
# 下記の様にすることで、カラムの名前を変更・置換可能
df.columns = ['Name', 'Position', 'Height']
print(df)
