class Solution:
    def repeatedCharacter(self, s: str) -> str:
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                return i
'''
Input: s = "abccbaacz"
Output: "c"

Input: s = "abcdd"
Output: "d"
'''