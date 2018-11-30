class Solution:
    def permute(self, nums):
        return self.permute_helper(nums, [], [])

    def permute_helper(self, nums, choosen, result):
        if nums is None or len(nums) == 0:
            result.append(list(choosen))
        else:
            for index, value in enumerate(nums):
                # choose
                ch = nums[index]
                del nums[index]
                choosen.append(ch)

                # Explore
                self.permute_helper(nums, choosen, result)

                # Unchoose
                nums.insert(index, value)
                choosen.pop()
        return result


s = Solution()
print(s.permute([1, 2, 3]))