class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       
        sum = 1
        sq  = [0]* len(nums)
        sq[0]=1 
        rq = [1]* len(nums)
        ans = []
        for  i in range(1,len(nums)):
            sq[i] = sq[i-1] * nums[i-1]
        for  i in range(len(nums)-2,-1,-1):
            rq[i] = rq[i+1] * nums[i+1]
        for i in range(len(nums)):
            ans.append(sq[i]*rq[i])
        return ans

        
            