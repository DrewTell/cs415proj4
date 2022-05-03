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
    print("(1a) Traditional Dynamic Programming Optimal value:", ansTask1A)
    print("(1a) Traditional Dynamic Programming Optimal subset:")
    print("(1a) Traditional Dynamic Programming Total Basic Ops:")



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
    #table creation for a 2 dimensional table of x values weight value
    #where y represents a different option
    table = [[0 for xCell in range(capacity + 1)] for yCell in range(size + 1)]
    for x in range(size + 1):                           
        for y in range(capacity + 1):                   
            if x == 0 or y == 0:
                table[x][y] = 0
            elif weight[x - 1] <= y:
                table[x][y] = max(value[x - 1] + table[x - 1][y - weight[x - 1]], table[x - 1][y])
            else:
                table[x][y] = table[x - 1][y]

    return table[size][capacity]  # returning the maximum value of knapsack    


if __name__ == "__main__":
    main()