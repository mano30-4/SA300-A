class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(s)
        left = 0
        for i in range(len(s)):
            if s[i]==" ":
                right = i-1
                print(s[right])
                while(left<right):
                    s[left],s[right]=s[right],s[left]
                    left+=1
                    right-=1
                left = i + 1
            if i == len(s)-1:
               right = i
               while(left<right):
                    s[left],s[right]=s[right],s[left]
                    left+=1
                    right-=1
        return "".join(s)

'''
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Input: s = "Mr Ding"
Output: "rM gniD"
'''