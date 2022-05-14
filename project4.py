

memWeight = []
memValues = []
memResult = []
memCounter = 0
def main():

    filesToOpen = fileToRead()

    print("File containing the capacity, weights, and values are:", filesToOpen[0], filesToOpen[1], filesToOpen[2], "\n")
    
    #filesToOpen[0] is the _c.txt file containing capacity
    #filesToOpen[1] is the _w.txt file and every weight will be added to the list
    #filesToOpen[2] is the _v.txt file and every value will be added to the list
    sackCapacity = capacity(filesToOpen[0])
    weightList = fileParser(filesToOpen[1])
    valueList = fileParser(filesToOpen[2])
    listSize = len(weightList)

    print("Knapsack capacity =", sackCapacity, "Total number of items =", listSize, "\n")

    task1A(sackCapacity, weightList, valueList, listSize)
    # task1B(sackCapacity, weightList, valueList, listSize)
    # task1C(sackCapacity, weightList, valueList, listSize)
    task2A(sackCapacity, weightList, valueList, listSize)
    task2B(sackCapacity, weightList, valueList, listSize)


def task1A(sackCapacity, weightList, valueList, listSize):
    
    ansTask1A = traditionalKnapSack(sackCapacity, weightList, valueList, listSize)
    print("(1a) Traditional Dynamic Programming Optimal value:", ansTask1A[0])
    print("(1a) Traditional Dynamic Programming Optimal subset:", ansTask1A[1])
    print("(1a) Traditional Dynamic Programming Total Basic Ops:", ansTask1A[2], '\n')

def task1B(sackCapacity, weightList, valueList, listSize):
    #Memory functions utilize global variables to utilize the recurrence relationships without extra computations
    #on redundent calculations
    
    global memWeight, memValues, memResult, memCounter
    memWeight = [0]
    memWeight.extend(weightList)
    memValues = [0]
    memValues.extend(valueList)

    memResult = [[-1 for spanOfCapacity in range(sackCapacity + 1)] for entriesAMT in range(listSize + 1)]

    for entryX in range(sackCapacity + 1):
        memResult[0][entryX] = 0
    for entryY in range(listSize + 1):
        memResult[entryY][0] = 0

    ansTask1B = memFuncKnapSack(listSize, sackCapacity)
    print("(1b) Memory-function Dynamic Programming Optimal value:", ansTask1B)
    print("(1b) Memory-function Dynamic Programming Optimal subset:", memFuncIndexes(listSize, sackCapacity))
    print("(1b) Memory-function Dynamic Programming Total Basic Ops:", memCounter, '\n')

def task1C(sackCapacity, weightList, valueList, listSize):
    
    ansTask1C = spaceEfficientKnapSack(sackCapacity, weightList, valueList, listSize)
    print("(1c) Space-efficient Dynamic Programming Optimal value:", ansTask1C[0])
    print("(1c) Space-efficient Dynamic Programming Optimal subset:", ansTask1C[1])
    print("(1c) Space-efficient Dynamic Programming Total Basic Ops:", ansTask1C[2], '\n')
    print("(1c) Space-efficient Dynamic Programming Space Taken:", ansTask1C[3], '\n')

def task2A(sackCapacity, weightList, valueList, listSize):
    
    anstask2A = greedyApproach(sackCapacity, weightList, valueList, listSize)
    print("(2a) Greedy Approach Optimal value:", anstask2A[0])
    print("(2a) Greedy Approach Optimal subset:", anstask2A[1])
    print("(2a) Greedy Approach Total Basic Ops:", anstask2A[2], '\n')

def task2B(sackCapacity, weightList, valueList, listSize):
    
    ansTask2B = heapBased(sackCapacity, weightList, valueList, listSize)
    print("(2b) Heap-based Greedy Approach Optimal value:", ansTask2B[0])
    print("(2b) Heap-based Greedy Approach Optimal subset:", ansTask2B[1])
    print("(2b) Heap-based Greedy Approach Total Basic Ops::", ansTask2B[2], '\n')

def fileToRead():
    #returns the file names to be used given an integer
    prefix = int(input("Enter a number to open associated files:"))
    nameGeneric = "p0"
    if (prefix > 9):
        nameGeneric = nameGeneric.rstrip("0")
    nameGeneric = nameGeneric + str(prefix)
    fileCap = nameGeneric + "_c.txt"
    fileWeight = nameGeneric + "_w.txt"
    fileValue = nameGeneric + "_v.txt"
    return fileCap, fileWeight, fileValue

def capacity(fileName):
    # capacity opens the _w.txt file to read the first value for the total weight that can be held
    fileData = open(fileName, 'r')
    capacity = fileData.read()
    fileData.close()
    return int(capacity)

def fileParser(fileName):
    # creates a list of values from a text file
    fileData = open(fileName, 'r')
    weightSet = []
    for x in fileData:
        weightSet.append(int(x.rstrip()))
    fileData.close()
    return weightSet

def traditionalKnapSack(capacity, weight, value, size):
    #table creation for a 2 dimensional table where capacity + 1 will create x cells for each integer up to capacity
    #ex capacity = 3: span will be 0,1,2,3
    #range of size will dictate how many rows there are in the 2-dimensional array
    numOfOps = 0
    table = [[0 for spanOfCapacity in range(capacity + 1)] for entriesAMT in range(size + 1)]
    

    for x in range(size + 1):                           
        for y in range(capacity + 1):                   
            if x == 0 or y == 0:
                table[x][y] = 0
                numOfOps = numOfOps + 1
            elif weight[x - 1] <= y:
                table[x][y] = max(value[x - 1] + table[x - 1][y - weight[x - 1]], table[x - 1][y])
                #comparison
                numOfOps = numOfOps + 1
            else:
                table[x][y] = table[x - 1][y]

    #After iterating through the whole table the best values will trickle down to the last cell of the table
    #located at (capacity, size) where capacity is the max hold limit in weight and size is the amt of entries

    maxValue = tempMaxValue = table[size][capacity]

    #The following segment is to extract the set that was derived from the table
    #The tempCapacity will decrease as we backtrack up the table everytime an item is found to be used
    # tempMaxValue = table[size][capacity]
    tempCapacity = capacity
    # resultSet = {}
    itemIndexes = []

    #declaring variables
    numOfOps += 3


    for i in range(size, 0, -1):
        if tempMaxValue <= 0:
            #comparison
            numOfOps += 1
            break
        elif tempMaxValue == table[i - 1][tempCapacity]:
            #comparison
            numOfOps += 1
            continue
        else:
            itemIndexes.append(i)
            tempMaxValue -= value[i-1]
            tempCapacity -= weight[i-1]

    itemIndexes.reverse()


    return maxValue, itemIndexes, numOfOps   # returning the maximum value of knapsack and the index of items in the table where the first item is item 1    

def memFuncKnapSack(listSize, sackCapacity):
    #needed to not reference local copies of the variable
    global memWeight, memValues, memResult, memCounter
    tempValue = 0

    if memResult[listSize][sackCapacity] < 0:
        memCounter = memCounter + 1
        if sackCapacity < memWeight[listSize]:
            #conditional comparison
            memCounter = memCounter + 1
            tempValue = memFuncKnapSack(listSize - 1, sackCapacity)
        else:
            #max comparison
            memCounter = memCounter + 1
            tempValue = max(memFuncKnapSack(listSize - 1, sackCapacity), memValues[listSize] + memFuncKnapSack(listSize - 1, sackCapacity - memWeight[listSize]))
        memResult[listSize][sackCapacity] = tempValue
    return memResult[listSize][sackCapacity]

def memFuncIndexes(listSize, sackCapacity):
    global memWeight, memValues, memResult, memCounter
    numOfOps = 0
    maxValue = tempMaxValue = memResult[listSize][sackCapacity]
    tempCapacity = sackCapacity
    itemIndexes = []
    for i in range(listSize, 0, -1):
        if tempMaxValue <= 0:
            memCounter += 1
            break
        elif tempMaxValue == memResult[i - 1][tempCapacity]:
            memCounter += 1
            continue
        else:
            itemIndexes.append(i)
            tempMaxValue -= memValues[i]
            tempCapacity -= memWeight[i]

    itemIndexes.reverse()
    return itemIndexes


#Global Variable for spaceEfficientKnapSack
HashTable = [[] for _ in range(10)]

def spaceEfficientKnapSack(capacity, weight, value, size):
    # Variables
    numOps = 0

    # Implement hash table with values.
    for i in range(capacity - 1):
        insert(HashTable, weight[i], value[i])
    

    print("PlaceHolder 1C")
    return 0, 0, 0, 0

# Hashing function to return the key for every value.
def Hashing(keyvalue):
    return keyvalue % len(HashTable)

# Insert Function to add values to the hash table
def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)


def greedyApproach(capacityVal, weightSet, valueSet, sizeVal):
    #zip is a python function that combines two arrays
    #into a tuple
    valueToWeightRatio = [value / weight for value, weight in zip(valueSet, weightSet)]
    itemIndex = []
    for i in range(sizeVal):
        itemIndex.append(i + 1)

    greedyMergeSortA(valueToWeightRatio, itemIndex)
    # valueToWeightRatio.extend([0])
    # valueSet.extend([0])
    # weightSet.extend([0])

    tempCapacity = capacityVal
    totalValue = stopIndex = 0
    for i in range(sizeVal):
        currentWT = weightSet[i]
        currentValue = valueSet[i]
        if tempCapacity - currentWT >= 0:
            tempCapacity = tempCapacity - currentWT
            totalValue = totalValue + currentValue
            stopIndex = i
        else:
            break 
    itemIndex = itemIndex[:stopIndex + 1]

    return totalValue, itemIndex, 0

def greedyMergeSortA(valToWeightArray, indexArray):
    if len(valToWeightArray) > 1:
        middle = len(valToWeightArray) // 2

        #Left and right array of ratios
        Left = valToWeightArray[:middle]
        Right = valToWeightArray[middle:]
        
        valueLeft = indexArray[:middle]
        valueRight = indexArray[middle:]
    
        greedyMergeSortA(Left, valueLeft) 
        greedyMergeSortA(Right, valueRight)

        i = j = k = 0

        while i < len(Left) and j < len(Right):
            if Left[i] > Right[j]:
                valToWeightArray[k] = Left[i]
                indexArray[k] = valueLeft[i]
                i = i + 1
            else:
                valToWeightArray[k] = Right[j]
                indexArray[k] = valueRight[j]
                j = j + 1
            k = k + 1
        while i < len(Left):
            valToWeightArray[k] = Left[i]
            indexArray[k] = valueLeft[i]
            i = i + 1
            k = k + 1
        while j < len(Right):
            valToWeightArray[k] = Right[j]
            indexArray[k] = valueRight[j]        
            j = j + 1
            k = k + 1

def heapBased(capacity, weight, value, size):
    print("PlaceHolder 2B")
    objectArr = []
    for index in range(size):
        tempItem = item(index + 1, value[index], weight[index])
        objectArr.append(tempItem)

    build_max_heap(objectArr)
    tempValue = stopIndex = 0
    tempWeight = capacity

    for i in range(size):
        currentWT = objectArr[i].get_data()[2]
        currentValue = objectArr[i].get_data()[1]
        if tempWeight - currentWT >= 0:
            tempWeight = tempWeight - currentWT
            tempValue = tempValue + currentValue
            stopIndex = i
        else:
            break 
    returnArray = []
    for i in range(stopIndex + 1):
        returnArray.append(objectArr[i].get_data()[0])
    return tempValue, returnArray, 0

class item:
    "This is an item class"
    def __init__(self, num, value, weight):
        self.itemNumber = num
        self.itemValue = value
        self.itemWeight = weight
    def get_data(self):
        return self.itemNumber, self.itemValue, self.itemWeight
    def get_itemRatio(self):
        return self.itemValue / self.itemWeight



def max_heapify(A,k):
    l = left(k)
    r = right(k)

    if l < len(A) and A[l].get_itemRatio() > A[k].get_itemRatio():
        largest = l
    else:
        largest = k
        
    if r < len(A) and A[r].get_itemRatio() > A[largest].get_itemRatio():
        largest = r
    if largest != k:
        A[k], A[largest] = A[largest], A[k]
        max_heapify(A, largest)

def left(k):
    return 2 * k + 1

def right(i):
    return 2 * i + 2

def build_max_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        max_heapify(A,k)








if __name__ == "__main__":
    main()