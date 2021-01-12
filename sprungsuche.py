import math
import sys
def sprungsuche(arr, x):

    m = math.floor(math.sqrt(len(arr)))
    print('m = ' + str(m))
    i = 1
    ende = False
    while ende == False:
        im = i * m
        print('\n\n '+str(i)+'. Schleifendurchlauf')
        print('i = '+str(i)+',   i * m = '+str(im))
        if (im)>= (len(arr)-1):
            ende = True
            im = len(arr)-1

        print('Ist x < L['+str(im)+']:  '+str(x)+' < '+str(arr[im])+'?', end = ' ')

        if x < arr[im]:
            print('Ja')
            print('     Dann Suche sequentiell in '+str(arr[((i - 1) * m):im]))

            sequientiellesuche(arr[((i-1)*m):(im)+1], x)
            return 0
        print('Nein')
        i = i + 1
    print('Ist letztes Element gesuchtes Element? ', end = ' ')
    if arr[len(arr)-1]==x:
        print('Ja')
        print('gefunden')
        return 0
    print('Nein')
    print('nicht gefunden')
def sequientiellesuche(arr, x):
    for i in range(len(arr)-1):
        print('             Ist x == L['+str(i)+'] ?', end = ' ')
        if x == arr[i]:
            print('Ja')
            print('gefunden')
            return 0
        print('Nein')
    print('nicht gefunden')
def StrToArray(str):
    arr = str[1:-1].split(',')
    print(arr)
    return arr

def main(argv):
    if (argv[1] == "-h"):
        print(f"USAGE:\n \t python sprungsuche.py <SortedArrray> <zuSuchendesElement> \n \n BSP: \n\t python sprungsuche.py [1,2,3,4] 3")
    else:
        sprungsuche(StrToArray(argv[1]), argv[2])
if __name__ == "__main__":
    main(sys.argv)

