#using set function 
def repeating_num(arr):
    seen = set()
    duplicate = set()
    for num in arr:
        if num in seen:
            duplicate.add(num)
        else:
            seen.add(num)
    return list(duplicate)

my_arr = [1,2,3,2,4,4,7]
result = repeating_num(my_arr)
print(result)
