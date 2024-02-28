from typing import List
#Time complexity=O(n^2) space complexity O(n)
class Solution:
    def findDisappearedNumbers1(self, nums):
        n = len(nums)
        ans = []
        for i in range(1, n+1):
            found = False
            for j in range(n):
                if i == nums[j]:
                    found = True
            if found == False:
                ans.append(i)
        return ans
    #Time complexity=O(n) space complexity O(1)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            i=abs(i)-1
            if  nums[i]>0:
                nums[i]*=-1
        ans=[]
        for i in range(len(nums)):
            if nums[i]>0:
                ans.append(i+1)
        return ans