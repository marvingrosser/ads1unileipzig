import sys
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

#Beispiel
def main(argv):
    if (argv[1] == "-h"):
        print(f"USAGE:\n \t python shellsort.py <Arrray>  \n \n BSP: \n\t python shellsort.py [1,2,3,4] ")
    else:
        shellsort(StrToArray(argv[1]))

def StrToArray(str):
    arr = str[1:-1].split(',')
    print(arr)
    return arr
if __name__ == "__main__":
    main(sys.argv)
