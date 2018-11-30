class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sarr = s.split(' ')
        for index, elem in enumerate(sarr):
            sarr[index] = elem[::-1]
        return ' '.join(sarr)


s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))