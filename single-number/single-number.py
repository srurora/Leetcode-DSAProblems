from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        table = collections.Counter(nums)
        for i in table:
            if table[i]==1: return i
        
        