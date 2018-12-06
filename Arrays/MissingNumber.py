class Solution:
    def missingNumber(self, nums):
        if nums is None: return None
        if len(nums) ==0: return False

        for index, value in enumerate(nums):
            if value != len(nums):
                nums[abs(value)] = -nums[abs(value)]
        for index, value in enumerate(nums):
            if value > 0:
                return index
        return len(nums)

s = Solution()
print(s.missingNumber([3,0,1]))
print(s.missingNumber([9,6,4,2,3,5,7,0,1]))
print(s.missingNumber([1]))
