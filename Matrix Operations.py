





def sumColumn(m, columnIndex):
    
    matrix = m 

    
    for column in range(len(matrix[0])):
        total = 0
        for row in range(len(matrix)):
            total += matrix[row][column]
        print("Sum for column", column, "is", float(total))



def main():
    matrix = [] # Create an empty list
    numberOfRows = 3 
    numberOfColumns = 4
    n = 0 
    for row in range(0, numberOfRows): 
        matrix.append([]) # Add an empty new row 
        
        value = (input("With space seperated values, enter a 4 values for a 3 by 4 matrix row " +str(n) +": "))
        n += 1
        value = value.split() 

        value = list(value) 
        value = [float(x) for x in value]

        for i in range(0,len(value)):
            matrix[row].append(value[i]) 
    sumColumn(matrix,1)


main() 
