nums = [int(x) for x in input('スペースを開けて十個数字を入力してください').split()]
counts = 0
for i in range(len(nums)):
    if nums[i] == 5:
        counts += 1
if counts > 0:
    print('５が含まれます')