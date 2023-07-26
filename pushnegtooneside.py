#pushuing all the negative elements to on side of the array
def pushnegative(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left]< 0:
            left+=1
        else:
            arr[left] , arr[right] = arr[right] , arr[left]
            right -= 1
    return arr
my_array = [-1,6,5,-2]
result = pushnegative(my_array)
print(result)
