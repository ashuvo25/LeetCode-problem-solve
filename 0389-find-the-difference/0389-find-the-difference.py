class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}
        for ch in t:
            count[ch] = count.get(ch, 0) + 1

        for ch in s:
            count[ch] = count.get(ch, 0) - 1

        for ch, c in count.items():
            if c > 0:
                return ch
        

        