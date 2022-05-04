def main():

    filesToOpen = fileToRead()
    print("File containing the capacity, weights, and values are:", filesToOpen[0], filesToOpen[1], filesToOpen[2], "\n")
    
    #filesToOpen[0] is the _c.txt file containing capacity
    sackCapacity = capacity(filesToOpen[0])

    #filesToOpen[1] is the _w.txt file and every weight will be added to the list
    #filesToOpen[2] is the _v.txt file and every value will be added to the list
    weightList = fileParser(filesToOpen[1])
    valueList = fileParser(filesToOpen[2])
    listSize = len(weightList)
    print("Knapsack capacity =", sackCapacity, "Total number of items =", listSize, "\n")
    ansTask1A = task1A(sackCapacity, weightList, valueList, listSize)
    print("File containing the capacy, weights, and values are:")
    print("(1a) Traditional Dynamic Programming Optimal value:", ansTask1A[0])
    print("(1a) Traditional Dynamic Programming Optimal subset:", ansTask1A[1])
    print("(1a) Traditional Dynamic Programming Total Basic Ops:", ansTask1A[2])



#returns the file names to be used given an integer
def fileToRead():
    prefix = int(input("Enter a number to open associated files:"))
    nameGeneric = "p0"
    if (prefix > 9):
        nameGeneric = nameGeneric.rstrip("0")
    nameGeneric = nameGeneric + str(prefix)
    fileCap = nameGeneric + "_c.txt"
    fileWeight = nameGeneric + "_w.txt"
    fileValue = nameGeneric + "_v.txt"
    return fileCap, fileWeight, fileValue

# capacity opens the _w.txt file to read the first value for the total weight that can be held
def capacity(fileName):
    fileData = open(fileName, 'r')
    capacity = fileData.read()
    fileData.close()
    return int(capacity)

# creates a list of values from a text file
def fileParser(fileName):
    fileData = open(fileName, 'r')
    weightSet = []
    for x in fileData:
        weightSet.append(int(x.rstrip()))
    fileData.close()
    return weightSet


def task1A(capacity, weight, value, size):
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


if __name__ == "__main__":
    main()