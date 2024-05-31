class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-1):
            for j in range(len(nums)):
                if(i<j and nums[i] == nums[j]):
                    count += 1
        return count     