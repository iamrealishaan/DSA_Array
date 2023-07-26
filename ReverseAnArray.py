def reverse_array(arr):
    if len(arr) < 2:
        return arr
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

# Testing The function
my_array = [1, 2, 3, 4, 5, 6, 7]
result = reverse_array(my_array)
print("The reversed array is:", result)
