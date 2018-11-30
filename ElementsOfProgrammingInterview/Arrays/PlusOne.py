class Solution:
    def plusOne(self, digits):
        if digits is None or len(digits) ==0: return digits
        carry = 0
        # case 1: Handle digit <= 8 and check carry
        # case 2: Handle digit == 9 and check carry

        for index, digit in reversed(list(enumerate(digits))):
            if index == len(digits) - 1:
                if digits[index] <= 8: digits[index] += 1
                else:
                    carry = 1
                    digits[index] = 0
            else:
                if digits[index] <= 8:
                    if carry == 1:
                        digits[index] += carry
                        carry = 0
                else:
                    if carry == 1:
                        digits[index] = 0
        if carry == 1:digits.insert(0, 1)

        return digits


s = Solution()
# print(s.plusOne([1, 2, 3]))
print(s.plusOne([9]))
print(s.plusOne([8, 9]))
print(s.plusOne([9, 9, 9]))
# print(s.plusOne([4, 3, 2, 1]))

