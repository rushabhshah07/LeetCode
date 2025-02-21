class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n*(n+1)//2
        array_sum = sum(nums)
        ans = expected_sum - array_sum
        return ans
        