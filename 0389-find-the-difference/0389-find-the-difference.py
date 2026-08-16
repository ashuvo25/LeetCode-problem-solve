class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        lis = {}
        for  i in s:
            if i in lis:
                lis[i]+=1
            else:
                lis[i] = 1
        for  i in t:
            if i in lis:
                lis[i]-=1
            else:
                lis[i] = 1
        for i in lis:
            if lis[i]:
                return i
        
        

        