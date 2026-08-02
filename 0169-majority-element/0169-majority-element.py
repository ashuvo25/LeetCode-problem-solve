class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq = 0
        val = nums[0]
        for i in range(len(nums)):
            if freq == 0:
                val = nums[i]

            if val == nums[i]:
                freq+=1
            else :
                freq -= 1
        return val