def find_min_chocolate_distribution(arr, m):
    n = len(arr)
    arr.sort()
    min_difference = float('inf')  # Initialize to a large value

    # Sliding window approach
    for i in range(n - m + 1):
        difference = arr[i + m - 1] - arr[i]
        min_difference = min(min_difference, difference)

    return min_difference

array = [3, 4, 1, 9, 56, 7, 9, 12]
m = 5
print(find_min_chocolate_distribution(array, m))
