class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
      dup=[]
      for i in arr:
       if len(dup)<len(arr):
        if i == 0:
            for j in range(2):
                dup.append(i)
        else:
            dup.append(i)
      for i in range(len(arr)):
        arr[i]=dup[i]

'''

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]

Input: arr = [1,2,3]
Output: [1,2,3]

Input:                  watch out test case breaks when we use len(dup) in last loop
[0,0,0,0,0,0,0]
Output
[0,0,0,0,0,0,0]
'''