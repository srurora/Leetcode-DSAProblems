class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = ''.join(str(e) for e in digits)
        y = int(x)+1
        y = str(y)
        arr = [int(e) for e in y]
        return arr
        