
def get_indices_of_item_wights(arr, limit):
    if not arr:
        return arr

    package_to_index = {}
    for j in range(0, len(arr)):
        diff = limit - arr[j]
        if diff in package_to_index:
            indexes = package_to_index[diff]
            return [j, indexes[len(indexes) - 1]]
        else:
            if arr[j] in package_to_index:
                package_to_index[arr[j]].append(j)
            else:
                package_to_index[arr[j]] = [j]


    return None


arr = [4,4,1]
print(get_indices_of_item_wights(arr, 5))
