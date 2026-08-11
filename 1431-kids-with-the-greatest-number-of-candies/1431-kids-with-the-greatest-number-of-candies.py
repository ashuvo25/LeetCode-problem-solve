class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ret = []
        mx = max(candies)
        for i in candies:
            if i+extraCandies >= mx:
                ret.append(True)
            else:
                ret.append(False)
        return ret

        