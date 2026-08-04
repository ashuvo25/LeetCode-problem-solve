class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        low = nums[0]
        big = nums[-1]
        seen = [False] * (big + 1)
        lis = []
        for i in nums:
            seen[i] = True
        for i in range(low , big):
            if seen[i] == False :
                lis.append(i)
        return lis