class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        for i in range(len(word)):
            if word[i] == ch :
                right = i
                left = 0
                while left<right :
                    word[left],word[right]=word[right],word[left]
                    left+=1
                    right-=1
                break
        return "".join(word)

    '''
Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"

Input: word = "xyxzxe", ch = "z"
Output: "zxyxxe"

Input: word = "abcd", ch = "z"
Output: "abcd
'''