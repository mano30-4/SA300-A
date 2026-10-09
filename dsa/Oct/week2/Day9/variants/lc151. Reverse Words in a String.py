class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(s)
        result=[]
        right=len(s)-1

        while right>=0:
            if s[right]==" ":
                right-=1
                continue

            left=right
            word=""

            while left>=0 and s[left]!=" ":
                word=s[left]+word
                left-=1

            result.append(word)
            right=left

        return " ".join(result)
'''
Input: s = "the sky is blue"
Output: "blue is sky the"

Input: s = "  hello world  "
Output: "world hello"

Input: s = "a good   example"
Output: "example good a"
'''