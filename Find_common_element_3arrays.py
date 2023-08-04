def find_common(a1, a2, a3):
    i, j, k = 0, 0, 0
    common_elements = []

    while i < len(a1) and j < len(a2) and k < len(a3):
        if a1[i] == a2[j] == a3[k]:
            common_elements.append(a1[i])
            i += 1
            j += 1
            k += 1
        elif a1[i] <= a2[j] and a1[i] <= a3[k]:
            i += 1
        elif a2[j] <= a1[i] and a2[j] <= a3[k]:
            j += 1
        else:
            k += 1

    return common_elements

array1 = [1, 3, 7, 9, 11]
array2 = [1, 3, 6, 11]
array3 = [1, 2, 4, 9, 11]
result = find_common(array1, array2, array3)
print(result)
