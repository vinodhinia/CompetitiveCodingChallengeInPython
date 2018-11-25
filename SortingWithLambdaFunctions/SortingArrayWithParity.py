def sortArrayPairing(A):
    A = A.sort(key=lambda a: a % 2)
    print(A)
    return A

arr = [3, 1, 15, 2]

print(sortArrayPairing(arr))