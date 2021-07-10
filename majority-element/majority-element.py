class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums: return 
        if len(nums)==1: return nums[0]
        nums.sort()
        return nums[len(nums)//2]
        