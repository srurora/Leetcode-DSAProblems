class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            tsum = 0
            while n>0:
                n, dig = divmod(n,10)
                tsum+=dig**2
            return tsum
        s = n
        f = getNext(n)
        while f!=1 and s!=f:
            s = getNext(s)
            f = getNext(getNext(f))
        return f==1
        