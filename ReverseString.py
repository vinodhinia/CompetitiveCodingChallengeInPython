class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or s.strip() == "": return s
        start = 0
        end = len(s) - 1
        str_arr = list(s)
        while start < end:
            str_arr[start], str_arr[end] = str_arr[end], str_arr[start]
            start += 1
            end -= 1
        return ''.join(str_arr)

# "A man, a plan, a canal: Panama"
# "amanaP :lanac a ,nalp a ,nam A"

s = Solution()
print(s.reverseString("A man, a plan, a canal: Panama"))