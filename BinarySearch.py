class Solution:
    def binary_search(self, nums, target):
        # Given a Sorted array, return the index of the sorted element
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
        return -1


s = Solution()
nums = [1,4,6, 9, 12, 20, 99]
target = 9

print(s.binary_search(nums, target))
print(s.binary_search(nums, 1))
print(s.binary_search(nums, 99))
print(s.binary_search(nums, 4))
