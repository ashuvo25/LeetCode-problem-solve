class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for c in s : 
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        for  i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1

        