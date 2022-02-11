#User function Template for python3

'''
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
'''

def maxChainLen(arr, n):
   dp = [1 for i in range(n)]
   arr.sort(key=lambda x:(x.a,x.b))
   for i in range(1,n):
       for j in range(0,i):
           if arr[i].a>arr[j].b and dp[i]<dp[j]+1: dp[i] = dp[j]+1
   return max(dp)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

if __name__ =='__main__':
    tcs = int(input())

    for _ in range(tcs):
        n=int(input())

        arr=[int(x) for x in input().split()]

        Parr=[]

        i=0
        while n*2>i:

            Parr.append(Pair(arr[i],arr[i+1]))

            i+=2

        #print(Parr,len(Parr))

        print(maxChainLen(Parr, n))
# } Driver Code Ends