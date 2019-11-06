import math
def spruchsuche(arr, x):
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
            print('     Dann Suche sequentiell in'+str(arr[((i - 1) * m):im]))

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
def sequientiellesuche(arr, x):
    for i in range(len(arr)-1):
        print('             Ist x == L['+str(i)+'] ?', end = ' ')
        if x == arr[i]:
            print('Ja')
            print('gefunden')
            return 0
        print('Nein')
    print('nicht gefunden')

ar = [2,8,8,9,27,28,30,47,60,66,67,67,83,101,103,127,152,164,177,182,192,195,204,210,219,221,242,243,243,255,268,288]

spruchsuche(ar, 114)