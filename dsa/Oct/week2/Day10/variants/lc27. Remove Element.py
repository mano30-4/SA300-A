class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
      answer=[]
      for i in range(len(nums)):
        if nums[i] == val:
            continue
        else:
            answer.append(nums[i])
      for i in range(len(answer)):
        nums[i]=answer[i]
      return len(answer)
'''
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]'''