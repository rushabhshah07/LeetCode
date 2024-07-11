class Solution:
    def minimumSum(self, num: int) -> int:
        digit = [int(d) for d in str(num)]
        digit.sort()
        num1 = digit[0]*10 + digit[2]
        num2 = digit[1]*10 + digit[3]
        return num1 + num2