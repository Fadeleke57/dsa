
def wiggle_sort(nums):
    for i in range(1, len(nums)):
        if i % 2 == 1 and nums[i] < nums[i-1] or i % 2 == 0 and nums[i] > nums[i-1]:
            nums[i], nums[i-1] = nums[i-1], nums[i]
    return nums

def wiggle_sort2(nums):
    count = [0] * 5001

    for num in nums:
        count[num] += 1

    sortedNums = []

    #counting sort
    for i in range(len(count)):
        for _ in range(count[i]):
            sortedNums.append(i)
    
    left = (len(sortedNums) - 1) // 2
    right = len(sortedNums) - 1

    for i in range(len(nums)):
        if i % 2 == 0:
            nums[i] = sortedNums[left]
            left -= 1
        else:
            nums[i] = sortedNums[right]
            right -= 1

    return nums