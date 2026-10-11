class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        even=[]
        odd=[]
        for i in nums :
            if i % 2 ==0:
                even.append(i)
            else:
                odd.append(i)
        for i in odd:
            even.append(i)
        return even
'''
Input: nums = [3,1,2,4]
Output: [2,4,3,1]

Input: nums = [0]
Output: [0]
'''