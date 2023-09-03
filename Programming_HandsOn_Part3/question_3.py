x = int(input('１つ目の数字'))
y = int(input('２つ目の数字'))
calc = str(input('add or minus'))
if calc == 'add':
    answer = x + y
if calc == 'minus':
    answer = x - y
print(answer)
