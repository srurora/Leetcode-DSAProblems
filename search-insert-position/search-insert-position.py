class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if target in nums: return nums.index(target)
        else: 
            if n<=1:
                if target<nums[0]: return 0
                else: return 1
            elif target<nums[0]: return 0
            elif target>nums[n-1]: return n
            else:
                for i in range(n-1):
                    if target in range(nums[i], nums[i+1]):
                        return(i+1)
        