class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Complexity - O(N)
        # Space Complexity - O(N)
        nums_count = {}
        for n in nums:
            if n in nums_count:
                nums_count[n] = nums_count[n] + 1
            else:
                nums_count[n] = 1

        length = len(nums)
        for key, value in nums_count.items():
            if value > int(length / 2):
                return key
        return None

if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([3,2,3]))
    print(s.majorityElement([2,2,1,1,1,2,2]))