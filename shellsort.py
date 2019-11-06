def printwhere(array,x,y):
    list = ([])
    for i in range(len(array)):
        if i == y: list.append('|'+str(array[i])+'|')
        elif i == x: list.append('['+str(array[i])+']')
        else:
            list.append(str(array[i]))

    print(list)
def shellsort(arr):
    t=0
    sw = int(len(arr) / 2)
    while t< len(arr)-1:
        print(arr)
        t = 0
        for i in range(len(arr)-sw):
            printwhere(arr,i,i+sw)
            if arr[i]>arr[i+sw]:

                arr[i+sw], arr[i] = arr[i], arr[i+sw]

                print('Tausch')
            else:
                t=t+1
        sw = int(sw/2)
        if sw < 1: sw = 1
    return arr

ar = [2,5,8,7,3,1,0,8,9,10,38,11,15,123,75,2,34,32,65,23,45,7654,234,64,233]
print(ar)
print(shellsort(ar))