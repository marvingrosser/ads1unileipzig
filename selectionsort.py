def printwhere(array,x,y):
    list = ([])
    for i in range(len(array)):
        if i == y: list.append('|'+str(array[i])+'|')
        elif i == x: list.append('['+str(array[i])+']')
        else:
            list.append(str(array[i]))

    print(list)
def selectionsort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            printwhere(arr,min,j)

            if (arr[j])< arr[min]: min = j

        arr[i],arr[min] = arr[min],arr[i]
        print('tausch')
    return arr


ar=[2,6,8,3,34,3,4,7,3,1,7,4,2,3,9,0]
print(ar)
print(selectionsort(ar))