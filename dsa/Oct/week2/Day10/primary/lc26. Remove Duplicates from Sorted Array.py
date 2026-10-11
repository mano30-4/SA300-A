
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
      freq={}
      unique_elements=[]
      count = 0
      for i in nums :
        if i not in freq:
            freq[i]=1
            unique_elements.append(i)
            count=count+1
      for i in range(len(unique_elements)):
        nums[i]=unique_elements[i]
      return count
"""
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
"""