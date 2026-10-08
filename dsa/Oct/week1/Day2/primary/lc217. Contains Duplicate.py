class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        freq = {}
        for i in nums :
            if i not in freq :
              freq[i]=1
            else :
              return True
        return False
'''
Test cases:

Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''