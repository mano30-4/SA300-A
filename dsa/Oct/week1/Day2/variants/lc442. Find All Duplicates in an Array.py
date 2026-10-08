class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        freq ={}
        output=[]
        for i in nums:
            if i not in freq:
                freq[i]=1
            else :
                output.append(i)
        return output
'''
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Input: nums = [1,1,2]
Output: [1]

Input: nums = [1]
Output: []
'''