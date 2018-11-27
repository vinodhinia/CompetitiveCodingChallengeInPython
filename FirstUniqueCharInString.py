import collections

class Solution:
    def firstUniqChar(self, S):
        """
        :param s:
        :return:
        """
        char_to_count = collections.OrderedDict()
        for s in S:
            if s in char_to_count:
                char_to_count[s] = char_to_count[s] + 1
            else:
                char_to_count[s] = 1

        for key, value in char_to_count.items():
            if value == 1:
                return S.find(key)
        return None

    def first_unique_char(self, S):
        char_to_count = [0]*26
        for s in S:
            char_ascii = ord(s) - 97
            char_to_count[char_ascii] += 1

        for index, value in enumerate(S):
            char_ascii = ord(value) - 97
            if char_to_count[char_ascii] == 1:
                return index
        return -1

s = Solution()
print(s.firstUniqChar("loveleetcode"))
print(s.first_unique_char("loveleetcode"))