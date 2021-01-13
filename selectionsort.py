import sys
def printwhere(array,x,y):
    list = ([])
    for i in range(len(array)):
        if i == y: list.append('|'+str(array[i])+'|')
        elif i == x: list.append('['+str(array[i])+']')
        else:
            list.append(str(array[i]))

    print(list)
def selectionsort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            printwhere(arr,min,j)

            if (arr[j])< arr[min]: min = j

        arr[i],arr[min] = arr[min],arr[i]
        print('tausch')
    return arr


def main(argv):
    if (argv[1] == "-h"):
        print(f"USAGE:\n \t python selectionsort.py <Arrray>  \n \n BSP: \n\t python selectionsort.py [1,2,3,4] ")
    else:
        selectionsort(StrToArray(argv[1]))

def StrToArray(str):
    arr = str[1:-1].split(',')
    print(arr)
    return arr
if __name__ == "__main__":
    main(sys.argv)
