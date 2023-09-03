nums = [5, 4, 1, 8, 7, 3, 2, 6]

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    merge_sort(left)
    merge_sort(right)
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1
    while j < len(right):
        nums[k] = right[j]
        k += 1
        j += 1
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
    return nums
merge_sort(nums)
print(nums)