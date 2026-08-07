class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = len(nums)
        sum = 1
        sq  = [0]* a
        sq[0]=1 
        rq = [1]* a
        ans = []
        for  i in range(1,a):
            sq[i] = sq[i-1] * nums[i-1]
        for  i in range(a-2,-1,-1):
            rq[i] = rq[i+1] * nums[i+1]
        for i in range(a):
            ans.append(sq[i]*rq[i])
        return ans

        
            