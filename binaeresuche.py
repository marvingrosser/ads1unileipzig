import math
import sys
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

#Beispiel
def main(argv):
    if (argv[1] == "-h"):
        print(f"USAGE:\n \t python binaeresuche.py <sortedINTArrray> <INTSearchedElement>  \n \n BSP: \n\t python binaeresuche.py [1,1,2,3,4,6,8,9,11] 6 ")
    else:
        binsuche(StrToArray(argv[1]), int(argv[2]) , 0)

def StrToArray(str):
    arr = str[1:-1].split(',')
    intarr =[]
    for strarre in arr :
        intarr.append(int(strarre))
    return intarr
if __name__ == "__main__":
    main(sys.argv)

