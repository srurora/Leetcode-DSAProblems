class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        if needle not in haystack: return -1
        x = haystack.index(needle)
        return x
        
        