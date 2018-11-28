class Solution:
    def isAnagram(self, s, t):
        if s is None and t is None: return s
        if s is None and t is not None: return False
        if s is not None and t is None: return False

        s_arr = [0] * (26)
        t_arr = [0] * (26)

        for ch in s: s_arr[ord(ch) - 97] += 1
        for ch in t: t_arr[ord(ch) - 97] += 1

        return True if s_arr == t_arr else False


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "car"))