class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if A is None or len(A) == 0:
            return True
        i = 0
        j = 1
        while j < len(A) and A[i] == A[j] :
            j += 1

        if j == len(A): return True
        increase_flag = False

        if A[j] - A[i] > 0:
            increase_flag = True

        if increase_flag:
            while j < len(A) and i < len(A) - 1:
                if A[j] - A[i] < 0:
                    return False
                else:
                    i = j
                    j = j + 1
            return True
        else:
            while j < len(A) and i < len(A) - 1:
                if A[j] - A[i] > 0:
                    return False
                else:
                    i = j
                    j = j + 1
            return True


s = Solution()
# print(s.isMonotonic([1,2,2,3]))
print(s.isMonotonic([6,5,4,4]))
# print(s.isMonotonic([1,3,2]))
# print(s.isMonotonic([1,2,4,5]))
print(s.isMonotonic([1,1,1]))
print(s.isMonotonic([1,1,1,2]))
