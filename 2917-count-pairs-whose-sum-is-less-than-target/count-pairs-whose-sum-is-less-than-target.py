class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        """
         0 1 2 3 4
        -1 1 1 2 3
        2
        """
        nums.sort()
        j = len(nums) - 1
        i = 0
        a = 0
        while i<j:
            if nums[i] + nums[j] < target:
                a += j-i
                i+=1
            else:
                j-=1
        return a