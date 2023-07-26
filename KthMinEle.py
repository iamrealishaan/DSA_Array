#to find kth smallest elemnt in the given array where k is less than the actual lenth of the array
def getkmin(arr, k):
    if len(arr) < k:
        return "Error"
    arr.sort()
    return arr[k-1]
my_arr = [10,4,3,24,7,56,2,1]
result = getkmin(my_arr , 4)
print(result)

