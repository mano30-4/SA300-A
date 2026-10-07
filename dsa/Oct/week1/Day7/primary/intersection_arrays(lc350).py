class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
       freq1={}
       freq2={}
       intersection=[]
       #creating hashtables for frequency for each list individually
       for i in range(len(nums1)):
         if nums1[i] not in freq1:
            freq1[nums1[i]]=1
         else:
            freq1[nums1[i]]=freq1[nums1[i]]+1
       for i in range(len(nums2)):
         if nums2[i] not in freq2:
            freq2[nums2[i]]=1
         else:
            freq2[nums2[i]]=freq2[nums2[i]]+1
       #comparing both frequency hashmaps then appending minimum count into intersection list
       for i in freq1:
            if i in freq2:
                minimum = min(freq1[i],freq2[i])
                for j in range(minimum):
                    intersection.append(i)
       return intersection

'''
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
'''
