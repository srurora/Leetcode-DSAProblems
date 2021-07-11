class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        d = {3:"Fizz", 5:"Buzz"}
        for num in range(1,n+1):
            x = ''
            for key in d.keys():
                if num%key==0:
                    x+=d[key]
            if not x:
                x = str(num)
            ans.append(x)
        return ans