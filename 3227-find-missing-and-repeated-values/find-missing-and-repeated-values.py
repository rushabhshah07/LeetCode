class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # l = len(grid)
        # a = {i for i in range(1,l*l+1)}
        # ans = []
        # for i in range(l):
        #     for j in range(l):
        #         if grid[i][j] in a:
        #             a.remove(grid[i][j])
        #         else:
        #             ans.append(grid[i],[j])
        #     return ans + [list(l)[0]]

        n = len(grid)
        nums = {i for i in range(1, n * n + 1)}
        res = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] in nums:
                    nums.remove(grid[i][j])
                else:
                    res.append(grid[i][j])
        return res + [list(nums)[0]]