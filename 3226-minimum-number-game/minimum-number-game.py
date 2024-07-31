class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans  = []
        # while nums:
        #     a_min = min(nums)
        #     nums.remove(a_min)
        #     b_min = min(nums)
        #     nums.remove(b_min)
        #     ans.append(b_min)
        #     ans.append(a_min)
        
        # return ans
        arr = sorted(nums)
        i = 0
        while (i <len(arr)-1):
            ans.append(arr[i+1])
            ans.append(arr[i])
            i += 2
        return ans
