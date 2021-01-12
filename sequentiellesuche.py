import sys
def sequientiellesuche(arr, x):
    print(arr[0])
    for i in range(len(arr)):
        print('             Ist x == L['+str(i)+'] ?', end = ' ')
        if x == arr[i]:
            print('Ja')
            print('gefunden')
            return 0
        print('Nein')
    print('nicht gefunden')

def main(argv):
    if (argv[1] == "-h"):
        print(f"USAGE:\n \t python sequentiellesuche.py <Arrray> <zuSuchendesElement> \n \n BSP: \n\t python sequentiellesuche.py [1,2,3,4] 3")
    else:
        sequientiellesuche(StrToArray(argv[1]), argv[2])
def StrToArray(str):
    arr = str[1:-1].split(',')
    print(arr)
    return arr
if __name__ == "__main__":
    main(sys.argv)
