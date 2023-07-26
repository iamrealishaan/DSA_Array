#find maximum and minimum element in an array
def getMinMax(arr):
    arr.sort()
    minmax = {'Min': arr[0], 'Max' : arr[-1]}
    return minmax
my_arr = [10,20,30,15,1,0,12,13]
MinMax = getMinMax(my_arr)
print("The maximum number is :", MinMax["Max"])
print("The minimum number is :", MinMax["Min"])

