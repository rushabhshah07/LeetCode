class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        mid_position = len(nums)//2
        for i in range(len(nums)//2):
            ans.append(nums[i])
            ans.append(nums[i + mid_position])
        return ans

            