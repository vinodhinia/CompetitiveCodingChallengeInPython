class Solution:
    def judgeCircle(self, moves):
        dict = {}
        for move in moves:
            if move in dict:
                dict[move] += 1
            else:
                dict[move] = 1

        return dict.get('U') == dict.get('D') and dict.get('L') == dict.get('R')

s = Solution()
print(s.judgeCircle('UD'))
print(s.judgeCircle('LL'))
print(s.judgeCircle('LR'))
print(s.judgeCircle('RL'))
print(s.judgeCircle('UDLR'))
print(s.judgeCircle('RLUD'))