#Selection Sort
def selectionSort(nums):
    for i in range(len(nums)):
        last = len(nums)-i-1
        maxidx =getMaxidx(nums, 0, last)
        nums[last], nums[maxidx] = nums[maxidx], nums[last]
    return nums

def getMaxidx(nums, startidx, lastidx):
    max = startidx
    for i in range(startidx, lastidx + 1):
        if nums[i] > nums[max]: max = i
    return max

nums = [20, 12, 10, 15, 2]
print(selectionSort(nums))
    
