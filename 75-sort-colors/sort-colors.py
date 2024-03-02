class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()  #more complexity
        # print(nums)

#better complexity
        count0 = 0
        count1 = 0
        count2 = 0

        for num in nums:
            if num == 0:
                count0 += 1
            if num == 1:
                count1 += 1
            if num == 2:
                count2 += 1

        i = 0
        while(count0>0):
            nums[i] = 0
            i+=1 
            count0 -= 1
        while(count1>0):
            nums[i] = 1
            i+=1
            count1-=1
        while(count2>0):
            nums[i] = 2
            i+=1
            count2-=1