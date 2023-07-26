#minimum no of jumps required to reach the end of te array
def max_jumps(arr):
    n = len(arr)
    if n <= 1 :
        return arr
    max_reach = arr[0]
    steps = arr[0]
    jumps = 1

    for i in range(1,n):
        max_reach = max(max_reach , i+ arr[i])
        steps -=1
        if steps ==0:
            jumps+=1
            steps = max_reach-1

    return jumps
arr1 = [1,2,3,0,4]
result = max_jumps(arr1)
print(result)
