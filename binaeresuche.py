import math
def binsuche(arr, x, i):
    i = i+1
    print('\n\n')
    print('Rekursion Nr.: '+ str(i))
    print('Ist L[] leer ?: ', end=' ')
    if len(arr)==0:
        print('Ja')
        print( ' ----->  nicht gefunden')
    else:
        print('Nein')
        mid = int(math.floor(len(arr)/2))
        print('mid =  '+str(len(arr))+'/2'+' = '+str(mid))

        if x==arr[mid]:
            print(' -----> gefunden')
        if x<arr[mid]:
            print(str(x) + ' < ' + str(arr[mid]))
            print('Suche x=' + str(x) + '  in L[' + str(0) + ' . . .' + str(mid-1) + ']')
            binsuche(arr[0:mid],x, i)
        if x>arr[mid]:
            print(str(x) + ' > ' + str(arr[mid]))
            print('Suche x=' + str(x) + '  in L['+str(mid+1)+' . . .'+ str(len(arr)-1)   +']')
            binsuche(arr[mid+1:len(arr)],x, i)


ar = [2,8,8,9,27,28,30,47,60,66,67,67,83,101,103,127,152,164,177,182,192,195,204,210,219,221,242,243,243,255,268,288]

print(binsuche(ar,114, 0))
