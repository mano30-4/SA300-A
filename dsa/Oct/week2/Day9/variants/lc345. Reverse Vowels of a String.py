class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        left  = 0
        right =len(s)-1
        def isVowel(i):
            if i.lower()=='a'or i.lower( )=='e' or i.lower() == 'o' or i.lower() == "i" or i.lower() == "u":
                return True
            return False
        for i in range(len(s)):
            if isVowel(s[i]):
                left=i
                while left<right:
                    if isVowel(s[right]):
                        s[left],s[right]=s[right],s[left]
                        right-=1
                        break
                    right -=1
        return str
'''

Input: s = "IceCreAm"
Output: "AceCreIm"

Input: s = "leetcode"
Output: "leotcede"'''