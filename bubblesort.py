def printwhere(array,x,y):
    list = ([])
    for i in range(len(array)):
        if i == y: list.append('|'+str(array[i])+'|')
        elif i == x: list.append('['+str(array[i])+']')
        else:
            list.append(str(array[i]))

    print(list)
def bubblesort(arr):
    t=0
    while t< len(arr)-1:
        print(arr)
        t = 0
        for i in range(len(arr)-1):
            printwhere(arr,i,i+1)
            if arr[i]>arr[i+1]:

                arr[i+1], arr[i] = arr[i], arr[i+1]

                print('Tausch')
            else:
                t=t+1
    return arr


ar = [3,6,8,2,35,5,6,7,34,6,97,34,2,543,1]
print(ar)
print(bubblesort(ar))