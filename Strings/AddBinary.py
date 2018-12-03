class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 1. Make both Strings of equal length
        # 2. Add digits from least significant bit and go till the first one
        # 3. Keep track of carry
        # 0 + 0 => 0, carry = 0
        # 0 + 1 => 1 / 1+0 => 1, carry = 0
        # 1 + 1=> 1 carry = 1
        if a is None and b is not None: return b
        if a is not None and b is None: return a
        max_len = max(len(a), len(b))
        if len(a) < max_len:
            a = self.addZeros(a, max_len-len(a))
        elif len(b) < max_len:
            b = self.addZeros(b, max_len-len(b))

        carry = '0'
        result =''
        for i in range(max_len-1, -1, -1):
            if a[i] == '1' and b[i] == '1':
                if carry == '1':
                    result = '1' + result
                    carry = '1'
                else:
                    carry = '1'
                    result = '0'+result
            elif a[i] == '0' and b[i] == '0':
                if carry == '1':
                    result = '1'+result
                    carry = '0'
                else:
                    result = '0'+result
            elif a[i] is '0' or b[i] is '0':
                if carry == '1':
                    carry = '1'
                    result = '0'+result
                else:
                    carry = '0'
                    result = '1'+result

        if carry == '1':
            result = '1' + result
        return result


    def addZeros(self, str, length):
        while length is not 0:
            str = '0'+str
            length -= 1
        return str

s = Solution()
a = "11"
b = "1"

print(s.addBinary(a, b))
print(s.addBinary('1', '0'))
print(s.addBinary('111', '111'))