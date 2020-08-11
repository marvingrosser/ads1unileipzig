def devcon(arr,i, x):
    print('\n\n Rekursion Nr. '+str(x))
    print('L = '+str(arr))
    print('Wähle p als letztes Element von L')
    p = arr[len(arr)-1]
    print('p = '+str(p))
    L1 = ([])
    L2 = ([])
    print('L1 enthält alle Elemente aus L die kleiner als ')
    print('L2 enthätl alle Elemente aus L > P')
    for e in range(len(arr)-1):
        if arr[e]<p:
            L1.append(arr[e])
        if arr[e]>p:
            L2.append(arr[e])
    print('L1 = '+str(L1))
    print('L2 = ' + str(L2))
    print('Ist L1.length == i - 1: '+str(len(L1))+' == '+str(i-1)+' ?', end = '')
    if len(L1) == i-1:
        print('Ja')
        print('Kleinstes Element gefunden: ', end = ' ')
        return p
    print('Nein')
    print('Ist L1.length > i - 1: ' + str(len(L1)) + ' > ' + str(i - 1) + ' ?', end='')
    if len(L1) > i - 1:
        print('Ja')
        print('     --> Dann wende Verfahren auf L1 rekursiv an i =' + str(i))
        return devcon(L1,i, x+1)
    print('Nein')
    print('Ist L1.length < i - 1: ' + str(len(L1)) + ' < ' + str(i - 1) + ' ?', end='')
    if len(L1) < i - 1:
        print('Ja')
        print('     --> Dann wende Verfahren auf L2 rekursiv an i = i - 1 - L1.length = ' + str(i-1-len(L1)))
        return devcon(L2, i-1-len(L1), x+1)
    print('Nein\n FEHLER')
    
    
#Beispiel:
ar= [5,2,7,3,1,6,12,10,9,16]
print(devcon(ar, 5, 1))
