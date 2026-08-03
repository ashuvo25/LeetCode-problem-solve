class Solution:
    def findNumbers(self, nums: List[int]) -> int:
     num_count : int = 0
     for i in range(len(nums)):
        digit: int = nums[i]
        dc :int = 0
        while digit > 0:
            dc+=1
            digit = (digit//10)
        if dc % 2 == 0:
            num_count += 1
     return num_count
