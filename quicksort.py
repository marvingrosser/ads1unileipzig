import sys
def Quicksort(arr):

    if len(arr)==1:
        return arr
    liste1 = ([])
    liste2 = ([])

    for i in range(len(arr)-1):
        if arr[0]>arr[i+1]:
            liste1.append(arr[i+1])
        else:
            liste2.append(arr[i+1])
    if len(liste1)<=len(liste2):
        liste1.append(arr[0])
    else:
        liste2.append(arr[0])
    print(str(liste1)+str(liste2))
    arr= Quicksort(liste1) + Quicksort(liste2)

    return arr

def main(argv):
    if (argv[1] == "-h"):
        print(f"USAGE:\n \t python quicksort.py <Arrray>  \n \n BSP: \n\t python quicksort.py [1,2,3,4] ")
    else:
        print(Quicksort(StrToArray(argv[1])))

def StrToArray(str):
    arr = str[1:-1].split(',')
    print(arr)
    return arr
if __name__ == "__main__":
    main(sys.argv)

