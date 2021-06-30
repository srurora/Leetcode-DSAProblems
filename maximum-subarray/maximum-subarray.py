class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return nums
        if len(nums)==1: return nums[0]
        arr = [nums[0]]
        for i in range(1,len(nums)):
            x = max(nums[i], arr[i-1]+nums[i])
            arr.append(x)
        return max(arr)        