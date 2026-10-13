class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maximum = 0
        seen = set()

        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[i])
            maximum = max(maximum, len(seen))

        return maximum


'''
***
Input: s = "abcabcbb"
Output: 3

Input: s = "bbbbb"
Output: 1

Input: s = "pwwkew"
Output: 3
'''