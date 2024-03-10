class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = float('-inf')
        curr_sum = 0

        for num in nums:
            curr_sum += num

            if curr_sum > sum:
                sum = curr_sum
            if curr_sum<0 :
                curr_sum = 0
        return sum