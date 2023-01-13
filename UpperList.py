numbers = list(map(int, input().split()))


def upper_or_not(nums):
    check = nums[0]
    if len(nums) <= 0:
        return 'NO'
    for i in range(1, len(nums)):
        if nums[i] <= check:
            return 'NO'
        check = nums[i]
    return 'YES'


print(upper_or_not(numbers))
