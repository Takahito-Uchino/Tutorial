a, b = (int(x) for x in input('スペースを開けて２つ入力してください').split())
print(a, b)
c = a
a = b
b = c
print(a, b)