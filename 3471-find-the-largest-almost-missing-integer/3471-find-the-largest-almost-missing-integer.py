class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        frek = {}
        for i in nums:
            if i in frek:
                    frek[i]+=1
            else :
                    frek[i] = 1
        if  k == len(nums):
            return max(nums)
        elif k == 1: 
            maxi = -1
            for i in frek:
                if frek[i] == 1:
                    maxi = max(maxi,i) 
            return maxi 
        else:

            maxi = -1

            if frek[nums[0]] == 1:
                maxi = max(maxi, nums[0])

            if frek[nums[-1]] == 1:
               maxi = max(maxi, nums[-1])

            return maxi
            

            

        

        