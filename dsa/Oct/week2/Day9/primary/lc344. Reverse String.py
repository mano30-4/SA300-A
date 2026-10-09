class Solution:
    def reverseString(self, s: list[str]) -> None:
        right = 0
        left = len(s)-1
        while right < left :
            s[right],s[left]=s[left],s[right]
            right+=1
            left-=1
'''
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''