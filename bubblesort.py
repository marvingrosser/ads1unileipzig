import sys
def printwhere(array,x,y):
    list = ([])
    for i in range(len(array)):
        if i == y: list.append('|'+str(array[i])+'|')
        elif i == x: list.append('['+str(array[i])+']')
        else:
            list.append(str(array[i]))

    print(list)
def bubblesort(arr):
    t=0
    while t< len(arr)-1:
        print(arr)
        t = 0
        for i in range(len(arr)-1):
            printwhere(arr,i,i+1)
            if arr[i]>arr[i+1]:

                arr[i+1], arr[i] = arr[i], arr[i+1]

                print('Tausch')
            else:
                t=t+1
    return arr

def main(argv):
    if (argv[1] == "-h"):
        print(f"USAGE:\n \t python bubblesort.py <Arrray>  \n \n BSP: \n\t python bubblesort.py [3,4,1,2] ")
    else:
        print(bubblesort(StrToArray(argv[1])))

def StrToArray(str):
    arr = str[1:-1].split(',')
    print(arr)
    return arr
if __name__ == "__main__":
    main(sys.argv)

