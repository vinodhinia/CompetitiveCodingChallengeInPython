class Solution:
    def sortArrayByParityNaive(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if A is None or len(A) == 1:
            return A
        for i in range(0, len(A)-1):
            for j in range(i+1, len(A)):
                if(A[i]%2 != 0):
                    temp = A[i]
                    A[i] = A[j]
                    A[j]= temp
        return A


    def sortArrayByParity(self, A):
        if A is None or len(A) == 1:
            return A
        left = 0
        right  = len(A) - 1
        while left < right:
            if A[left]%2 != 0 and A[right]%2 == 0:
                temp = A[left]
                A[left] = A[right]
                A[right] = temp
                left += 1
                right -= 1
            elif A[left]%2 != 0 and A[right]%2 != 0:
                right -= 1
            else:
                left += 1
        return A


s = Solution()
print(s.sortArrayByParity([3,1,2,4]))

print(s.sortArrayByParity([3,1,9,13]))

print(s.sortArrayByParity([3,1,2,13]))

print(s.sortArrayByParity([13, 4,6,2]))


# 3,1,2,4
# IT 1 : [1, 3 , 2, 4]
# IT 2 : [2, 3, 1, 4]
# IT 3: []