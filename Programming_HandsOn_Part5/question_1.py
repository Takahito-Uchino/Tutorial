a = int(input('１つ目の正の整数値を入力'))
b = int(input('２つ目の正の整数値を入力'))

if a % b == 0 or b % a == 0:
    answer = False
else:
    answer = True
print(answer)