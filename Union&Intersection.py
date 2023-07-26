#finding the union and intersection of 2 sorted arrays
def findunionintersection(arr1,arr2):
    union = []
    intersection = []
    i = 0
    j = 0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            union.append(arr1[i])
            i+=1
        if arr1[i] > arr2[j]:
            union.append(arr2[j])
            j += 1
        else:
            union.append(arr1[i])
            intersection.append(arr1[i])
            i+=1
            j+=1
    while i<len(arr1):
        union.append(arr1[i])
        i+=1
    while j < len(arr2):
        union.append(arr2[j])
        j += 1
    return union,intersection
arr1 = [1,2,4,6,5]
arr2 = [1,2,3,4,5]
union,intersection = findunionintersection(arr1,arr2)
print(union)
print(intersection)
