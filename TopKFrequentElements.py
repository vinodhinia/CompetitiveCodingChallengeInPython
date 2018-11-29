class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) <= 1: return nums
        num_to_freq = {}
        for n in nums:
            if n in num_to_freq:
                num_to_freq[n] += 1
            else:
                num_to_freq[n] = 1

        result = [None] * (len(nums)+1)
        for key, value in num_to_freq.items():
            if result[value] is None:
                result[value] = [key]
            else:
                result[value].append(key)
        final = []
        for i in range(len(result)-1, 0, -1):
            if k > 0 and result[i] is not None:
                arr = result[i]
                for a in arr:
                    if k > 0:
                        final.append(a)
                        k -= 1
        return final


s = Solution()
nums = [1, 1, 1, 2, 2, 3]
print(s.topKFrequent(nums, 2))
print(s.topKFrequent([1], 1))
print(s.topKFrequent([-1, -1], 1))