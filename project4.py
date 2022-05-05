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
    task1B(sackCapacity, weightList, valueList, listSize)
    task1C(sackCapacity, weightList, valueList, listSize)
    task2A(sackCapacity, weightList, valueList, listSize)
    task2B(sackCapacity, weightList, valueList, listSize)

def task1A(sackCapacity, weightList, valueList, listSize):
    
    ansTask1A = traditionalKnapSack(sackCapacity, weightList, valueList, listSize)
    print("(1a) Traditional Dynamic Programming Optimal value:", ansTask1A[0])
    print("(1a) Traditional Dynamic Programming Optimal subset:", ansTask1A[1])
    print("(1a) Traditional Dynamic Programming Total Basic Ops:", ansTask1A[2], '\n')

def task1B(sackCapacity, weightList, valueList, listSize):
    
    ansTask1B = memFuncKnapSack(sackCapacity, weightList, valueList, listSize)
    print("(1b) Memory-function Dynamic Programming Optimal value:", ansTask1B[0])
    print("(1b) Memory-function Dynamic Programming Optimal subset:", ansTask1B[1])
    print("(1b) Memory-function Dynamic Programming Total Basic Ops:", ansTask1B[2], '\n')

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
    

    numOfOps = (capacity + 1) * (size + 1)

    for x in range(size + 1):                           
        for y in range(capacity + 1):                   
            
            if x == 0 or y == 0:
                table[x][y] = 0
                #setting value
                numOfOps += 1

            elif weight[x - 1] <= y:
                table[x][y] = max(value[x - 1] + table[x - 1][y - weight[x - 1]], table[x - 1][y])
                #comparison
                numOfOps += 1
            else:
                table[x][y] = table[x - 1][y]
                #setting Value
                numOfOps += 1

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
            # resultSet[i] = [weight[i-1], value[i-1]]
            itemIndexes.append(i)
            tempMaxValue -= value[i-1]
            tempCapacity -= weight[i-1]
            #setting values
            numOfOps += 3

    itemIndexes.reverse()


    return table[size][capacity], itemIndexes, numOfOps   # returning the maximum value of knapsack and the index of items in the table where the first item is item 1    

def memFuncKnapSack(capacity, weight, value, size):
    print("PlaceHolder 1B")
    return 0, 0, 0


def spaceEfficientKnapSack(capacity, weight, value, size):
    # Global variable for hash table.
    HashTable = [[] for i in range(capacity)]
    print("Capacity size: ", capacity)
    # Keep track of our number of operations.
    numOps = 0

    # Insert values into hash table.
    for i in range(capacity - 1):
        #print("Value: ", value[i])
        hash_key = spaceEfficientHelper(weight[i], HashTable)
        HashTable[hash_key].append(value[i])

    for i in range(capacity - 1):
        print(HashTable[i])


    print("PlaceHolder 1C")
    return 0, 0, 0, 0

def spaceEfficientHelper(keyvalue, HashTable):
    return keyvalue % len(HashTable)

def greedyApproach(capacity, weight, value, size):
    print("PlaceHolder 2A")
    return 0, 0, 0, 0

def heapBased(capacity, weight, value, size):
    print("PlaceHolder 2B")
    return 0, 0, 0


if __name__ == "__main__":
    main()