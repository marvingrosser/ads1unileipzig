import math
import sys
#Interpolationssuche

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

def StrToArray(str):
    arr = str[1:-1].split(',')
    intarr =[]
    for strarre in arr :
        intarr.append(int(strarre))
    return arr

def main(argv):
    if (argv[1] == "-h"):
        print(f"USAGE:\n \t python sprungsuche.py <SortedArrray> <zuSuchendesElement> \n \n BSP: \n\t python sprungsuche.py [1,2,3,4] 3")
    else:
        interpolsuche(StrToArray(argv[1]), int(argv[2]),0 ,len(StrToArray(argv[1])) -1, 1 )
if __name__ == "__main__":
    main(sys.argv)

