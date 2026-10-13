class Solution:
    def maxSubarraySum(self, arr, k):
        # code here
        window_sum = sum(arr[:k])
        maximum = window_sum
        for i in range(k, len(arr)):
            window_sum = window_sum + arr[i] - arr[i - k]
            maximum = max(maximum, window_sum)
        return maximum

'''
Input: arr[] = [100, 200, 300, 400], k = 2
Output: 700

Input: arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
Output: 39

Input: arr[] = [100, 200, 300, 400], k = 1
Output: 400 '''

## brute force
class Solution:
    def maxSubarraySum(self, arr, k):
        for i in range (len(arr)):
            addition = 0
            for j in range(i, i + k):
                if i+k < len(arr):
                    addition += arr[j]
            maximum = max(addition, maximum)
        return maximum 
