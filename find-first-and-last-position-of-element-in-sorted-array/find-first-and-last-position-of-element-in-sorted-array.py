class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        c = collections.Counter(nums)
        ans = []
        if c[target]==1:
            return [nums.index(target),nums.index(target)]
        elif c[target]==0:
            return [-1,-1]
        elif len(nums)==1 and target==nums[0]: return [0,0]
        else: return [nums.index(target), nums.index(target)+c[target]-1]
        