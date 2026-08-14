class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = [0] * 26
        last =0
        max_len = 0
        for i in range(len(s)):
            idx = ord(s[i]) - ord('a') 
            freq[idx ]+=1
            while freq[idx] > 2:
                last_char =  ord(s[last]) - ord('a') 
                freq[last_char]-=1
                last+=1
            max_len = max(max_len,i - last + 1)
            
        return max_len


        