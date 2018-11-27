class Solution:
    def groupAnagrams(self, strs):
        if strs is None or len(strs) ==0:
            return strs
        str_dict = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key in str_dict:
                str_dict[key].append(str)
            else:
                str_dict[key] =[str]

        return str_dict.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
print(s.groupAnagrams(strs))
