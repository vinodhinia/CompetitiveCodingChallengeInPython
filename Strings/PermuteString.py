class Solution:
    def permute(self, str):

        return self.permute_helper(str, '', [])


    def permute_helper(self, str, choosen, result):
        if str is None or str is '':
            result.append(choosen)
            # print(choosen)

        for i in range(0, len(str)):
        # choose
            ch = str[i]
            choosen += ch
        # Explore
            str = str[:i] + str[i+1:]
            self.permute_helper(str, choosen, result)
        # Unchoose
            str = str[:i] + ch + str[i:]
            choosen = choosen[:-1]

        return result

s = Solution()
print(s.permute("123"))