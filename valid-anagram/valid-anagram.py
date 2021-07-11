class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = collections.Counter(s)
        y = collections.Counter(t)
        return x==y