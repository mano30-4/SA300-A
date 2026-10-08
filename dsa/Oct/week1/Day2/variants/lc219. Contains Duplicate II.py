class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
     freq={}
     for i in range(len(nums)):
        if nums[i] not in freq :
            freq[nums[i]]=i
        elif abs(i-freq[nums[i]])<=k:
            return True
        else: ## helps in test case 2 because we need update freq[nums[i]] value if ther is more than one duplicate and if it doesn't statisfy abs(i-freq[nums[i]])<=k
            freq[nums[i]]=i
     return False

'''
Input: nums = [1,2,3,1], k = 3
Output: true

Input: nums = [1,0,1,1], k = 1
Output: true

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

'''