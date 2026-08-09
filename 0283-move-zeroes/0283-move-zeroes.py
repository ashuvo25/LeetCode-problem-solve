class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i  = j = 0
        for  k in range(len(nums)):
            if nums[i]!= 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i+=1
                j+=1
            else:
                i+=1
        return nums

        