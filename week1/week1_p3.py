class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hash = {0:0, 1:0, 2:0}
        for i in nums:
            hash[i] += 1

        for i in range(0, len(nums)):
            if i < hash[0]:
                nums[i] = 0
            elif i < (hash[0] + hash[1]):
                nums[i] = 1
            else:
                nums[i] = 2