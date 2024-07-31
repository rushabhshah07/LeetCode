class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans  = []
        while nums:
            a_min = min(nums)
            nums.remove(a_min)
            b_min = min(nums)
            nums.remove(b_min)
            ans.append(b_min)
            ans.append(a_min)
        
        return ans