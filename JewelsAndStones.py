class Solution:
    def numJewelsInStones(self, J, S):
        """

        :param J:
        :param S:
        :return: int
        """
        stones_count = {}
        for s in S:
            if s in stones_count:
                stones_count[s] = stones_count[s] + 1
            else:
                stones_count[s] = 1

        total = 0
        for j in J:
            if j in stones_count:
                total += stones_count[j]
        return total

    def num_jewels_in_stones(self, J, S):
        if J is None or S is None: return 0
        total = [s for s in S if s in J]
        return len(total)

s = Solution()
print(s.numJewelsInStones("aA", 'aAAbbbb'))
print(s.numJewelsInStones("z", 'ZZZZ'))


print(s.num_jewels_in_stones("aA", 'aAAbbbb'))
print(s.num_jewels_in_stones("z", 'ZZZZ'))