##643. Maximum Average Subarray I

## optimised solution O(n)
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        summation = sum(nums[:k])
        average = summation / k
        maximum = average
        left = 0

        for i in range(k, len(nums)):
            summation = summation + nums[i] - nums[left]
            left = left + 1
            average = summation / k
            maximum = max(average, maximum)
        maximum = round(maximum,5)
        return maximum


## brute force: O(n^2)
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
      Maximum = 0
      for i in range(len(nums)):
        summation = 0
        for j in range(i,i+k):
          if i+k <= len(nums):
            summation = summation + nums[j]
        average = summation / k
        Maximum=max(Maximum,average)
      Maximum = round(Maximum,5)
      return Maximum

##implementation functions:

    def add(a:list):
        addition = 0
        for i in a :
            addition +=1
        return addition

    def maximum(a,b):
        if a>b :
           return a
        return b

'''
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000

Input: nums = [5], k = 1
Output: 5.00000
'''