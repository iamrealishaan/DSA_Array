#Program to cyclically rotate an array by one
def rotate(arr):
    if len(arr) <=1:
        return arr
    end = arr[-1]
    for i in range(len(arr)-1 , 0 ,-1):
        arr[i] = arr[i-1]
    arr[0] = end
    return arr
my_arr = [1,2,3,4,5]
result = rotate(my_arr)
print(result)
