class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_output = 0
        for i in range(len(accounts)):
            total = sum(accounts[i])
            max_output = max(total, max_output)
        return max_output
