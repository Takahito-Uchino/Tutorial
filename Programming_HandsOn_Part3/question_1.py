nums = [int(x) for x in input('スペースを開けて十個の数字を入力してください').split()]
counts = 0
for i in range(len(nums) - 1):
    if nums[i + 1] == nums[i]:
        counts += 1
if counts == 9:
    counts = 'perfect'
print(counts)