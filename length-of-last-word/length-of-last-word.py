class Solution:
    def lengthOfLastWord(self, s: str) -> int:
            self.s = s
            l = s.split(" ")
            s = 0
            for i in l[::-1]:
                if(i == ''):
                    continue
                else:
                    s = len(i)
                    break
            return s