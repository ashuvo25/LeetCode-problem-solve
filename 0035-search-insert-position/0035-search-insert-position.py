class Solution:

    def binary_search(self, arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target)