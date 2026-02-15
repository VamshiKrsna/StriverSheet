def bubbleSort(arr:list)->list: 
    counter = 0 
    n = len(arr) 
    for i in range(n):
        counter += 1
        for j in range(n-1):
            counter += 1
            if arr[j] > arr[j+1]:
                swap(arr[j], arr[j+1]) 
    print(counter)
    return arr

def swap(a:int, b:int): 
    temp = b 
    b = a 
    a = temp 

if __name__ == "__main__":
    print("hello")
    print(bubbleSort([15,10,1]))