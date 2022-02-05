# Function should return an integer value
def convertFive(n):
    # Code here
    num = str(n)
    ans = []
    for i in range(len(num)):
        if num[i]=='0': ans.append(5)
        else: ans.append(num[i])
    return int(''.join(str(e) for e in ans))
    
#{ 
#  Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        print (convertFive(int(input().strip())))
# } Driver Code Ends