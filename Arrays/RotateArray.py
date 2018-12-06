class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None:return None
        length = len(nums)
        result = [0]*(len(nums))
        for index, num in enumerate(nums):
            if index + k >= length:
                move_index = (index + k) % length
                result[move_index] = num
            else:
                result[index+k] = num
        return result


s = Solution()
print((s.rotate([1,2,3,4,5,6,7], 3)) == [5,6,7,1,2,3,4])
print((s.rotate([-1,-100,3,99], 2)) == [3,99,-1,-100])
print(s.rotate([1,2,3,4], 4))








#[1,2,3,4,5,6,7], 3
# 0 1 2 3 4 5 6
#[7,1,2,3,4,5,6]
#[6,7,1,2,3,4,5]
#[5,6,7,1,2,3,4]
# 0 1 2 3 4 5 6
#
#   0 => 3
#   1 => 4
#   2 => 5
#   3 => 6
#   4 => 0
#   5 => 1
#   6 => 2
#
#
# index + k => crosses the max index then calculate diff
# len = 7
# 6+3%7 => 2
# 5 + 3 %7 => 1
# 4 + 3%7 => 0
