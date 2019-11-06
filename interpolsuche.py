import math


def interpolsuche(arr, x, u , v, i):
    print('\n\n')
    print('Rekursionsaufruf Nr: ' + str(i))
    print('L =  '+str(arr[u:v]))
    print('Ist L[] leer ?: ', end=' ')
    if len(arr[u:v]) == 0:
        print('Ja')
        print(' ----->  nicht gefunden')
    else:
        print('Nein')
        print('mid =  u + (x - L[u])/(L[v] - L[u]) * (v - u) = ' + str(u) + ' + (' + str(x) + ' - ' + str(
            arr[u]) + ')/(' + str(arr[v]) + ' - ' + str(arr[u]) + ') * (' + str(v) + ' - ' + str(u) + ')' + ' =' , end= ' ')
        if arr[v]-arr[u]<=0:
            print('Nicht lösbar --> nicht gefunden')
            return 0

        mid = int(math.floor(u+((x-arr[u])/(arr[v]-arr[u]))*(v-u)))
        print(mid)
        if x == arr[mid]:
            print('gefunden')
        if x < arr[mid]:
            print('Da x > L[mid] :  '+str(x)+' < '+str(arr[mid]))
            print('Suche x='+str(x)+'  in L[], u =' +str(u)+ ', v='+str(mid-1))
            interpolsuche(arr, x, u , mid-1, i+1)
        if x > arr[mid]:
            print('Da x < L[mid] :  '+str(x) + ' > ' + str(arr[mid]))
            print('Suche x=' + str(x) + '  in L[], u =' + str(mid+1) + ', v=' + str(v))
            interpolsuche(arr, x, mid+1, v, i+1)


ar = [2,8,8,9,27,28,30,47,60,66,67,67,83,101,103,127,152,164,177,182,192,195,204,210,219,221,242,243,243,255,268,288]

print(interpolsuche(ar,114, 0, 31, 1))
