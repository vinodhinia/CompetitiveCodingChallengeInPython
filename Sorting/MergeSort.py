class Solution:
    def sort(self, arr):
        if len(arr) <= 1: return arr
        length = len(arr)
        left_arr_size = int(length/2)
        right_arr_size = length - int(length/2)
        left = []*(length/2)
        right = []*(length - (length/2))
        i = 0
        for i in range(0, left_arr_size):
            left.append(arr[i])
        i = i+1
        for i in range(i, len(arr)):
            right.append(arr[i])
        left = self.sort(left)
        right = self.sort(right)

        return self.merge(left, right)

    def merge(self, arr1, arr2):
        if arr1 is None and arr2 is not None:
            return arr2
        elif arr1 is not None and arr2 is None:
            return arr1
        result = []*(len(arr1) + len(arr2))
        a1 = 0
        a2 = 0

        while a1 < len(arr1) and a2 < len(arr2):
            if arr1[a1] < arr2[a2]:
                result.append(arr1[a1])
                a1 += 1
            elif arr1[a1] == arr2[a2]:
                result.append(arr1[a1])
                result.append(arr2[a2])
                a1 += 1
                a2 += 1
            else:
                result.append(arr2[a2])
                a2 += 1
        while a1 < len(arr1):
            result.append(arr1[a1])
            a1 += 1
        while a2 < len(arr2):
            result.append(arr2[a2])
            a2 += 1
        return result


s = Solution()
arr = [8, 4, 7, 1, 10]
arr1 = [1, 8, 10]
arr2 = [4, 7]

print(s.sort(arr))
print(s.merge(arr1, arr2))
# [1, 4, 7, 8, 10]
# [1, 8, 10] [4, 7]
