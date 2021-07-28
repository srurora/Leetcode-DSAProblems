class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = collections.Counter(nums)
        nums = list(counter.keys())
        res = set()
        if counter[0]>=3: res.add((0,0,0))
        pos, neg = [x for x in nums if x>0], [y for y in nums if y<0]
        for i in neg:
            for j in pos:
                c = -(i+j)
                if c in counter and ((c!=i and c!=j) or counter[c]>1):
                    res.add(tuple(sorted([i,j,c])))
        return res
        