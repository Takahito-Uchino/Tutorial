bottom = int(input('底辺を入力してください'))
height = int(input('高さを入力してください'))

for i in range(1,height+1):
    if i == 1:
        print('*' * bottom, '\n')
    elif i > 1 and i < height:
        print('*', ' ' * (bottom - 4), '*', '\n')
    elif i == height:
        print('*' * bottom)