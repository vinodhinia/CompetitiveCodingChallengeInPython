class Solution:
    def subsets(self, nums):
        result = [[]]
        for n in nums:
            temp_result = result[:]
            for res in result:
                temp_arr = res[:]
                temp_arr.append(n)
                if temp_arr not in temp_result:
                    temp_result.append(temp_arr)
            result = temp_result[:]
        return result
#
# [1,2,3]
# [[]]
#1. tem_Arr = [] => [1]

s = Solution()
print(s.subsets([1, 2, 3]))