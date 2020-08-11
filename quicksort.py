def Quicksort(arr):

    if len(arr)==1:
        return arr
    liste1 = ([])
    liste2 = ([])

    for i in range(len(arr)-1):
        if arr[0]>arr[i+1]:
            liste1.append(arr[i+1])
        else:
            liste2.append(arr[i+1])
    if len(liste1)<=len(liste2):
        liste1.append(arr[0])
    else:
        liste2.append(arr[0])
    print(str(liste1)+str(liste2))
    arr= Quicksort(liste1) + Quicksort(liste2)

    return arr

#Beispiel
arr = [0,4,8,9,32,4,3,123,54,436,645,63,3,5,8,978,56,324,4,3,435,653,45,7,63,3,3,323,3]
print(arr)
print(Quicksort(arr))
