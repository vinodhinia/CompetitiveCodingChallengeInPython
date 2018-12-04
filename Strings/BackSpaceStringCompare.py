class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        if S is None and T is None: return True
        if S is None or T is None: return True

        return self.removeBackSpace(S) == self.removeBackSpace(T)

    def removeBackSpace(self, str):
        while str.find('#') != -1:
            index = str.find('#')
            if index == 0:
                str = str[1:]
            else:
                if index + 1 != len(str):
                    str = str[0:index-1] + str[index+1:]
                else:
                    str = str[0:index-1]
        return str

    def backspaceCompareBestApproach(self, S, T):
        def bsString(string):
            list = []
            for s in string:
                if s != '#':
                    list.append(s)
                else:
                    list = list[:-1]
            return list
        return bsString(S) == bsString(T)


s = Solution()
print(s.backspaceCompare("ab#c","ad#c"))
print(s.backspaceCompare("ab##","c#d#"))
print(s.backspaceCompare("a##c","#a#c"))
print(s.backspaceCompare("a#c","b"))


print(s.backspaceCompareBestApproach("ab#c","ad#c"))
print(s.backspaceCompareBestApproach("ab##","c#d#"))
print(s.backspaceCompareBestApproach("a##c","#a#c"))
print(s.backspaceCompareBestApproach("a#c","b"))