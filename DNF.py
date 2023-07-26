#Dutch National Flag problem
#sort array of 0's 1's and 2's
def Dutch_national_flag(arr):
    low= 0
    mid = 0
    high = len(arr)-1
    while mid<=high:
        if arr[mid] == 0:
            arr[low] , arr[mid] = arr[mid], arr[low]
            low+=1
            mid+=1
        elif arr[mid] ==1:
            mid+=1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high-=1
    return arr
my_array = [0,1,2,2,2,1,0]
result = Dutch_national_flag(my_array)
print(result)
