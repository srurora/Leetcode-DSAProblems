from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dict = Counter(p)
        len_p = len(p)
        x = s[:len_p]
        s_dict = Counter(x)
        ans = []
        if s_dict==p_dict: ans.append(0)
        for i in range(1,len(s)-len_p+1):
            first = s[i-1]; end = s[i+len_p-1]
            if end not in s_dict: s_dict[end]=1
            else: s_dict[end]+=1
            if s_dict[first]==1: del s_dict[first]
            else: s_dict[first]-=1
            if s_dict==p_dict: ans.append(i)
        return ans
            
        