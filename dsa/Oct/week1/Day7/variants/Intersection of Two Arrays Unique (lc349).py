class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        output=[]
        nums1=list(set(nums1))
        print(nums1)
        for i in nums1:
            if i in nums2:
                output.append(i)
        return output
'''
test cases:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]'''