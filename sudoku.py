def isComplete(blanks):

    complete = True
    for item in blanks:
        if item[1] == False:
            complete = False

    return complete


def isValid(grid,blanks):

    check_grid = grid
    for blank in blanks:
        check_grid[blank[0][0]][blank[0][1]]=blank[1]

    for row in check_grid:
        if duplicatesExist(row):
            return False

    for i in range(0,len(grid)):
        if duplicatesExist([row[i] for row in grid]):
            return False

    for i in range(0,7,3):
        for j in range(0,7,3):
            lis = []
            for x in range(i,i+3):
                for y in range(j,j+3):
                    lis.append(check_grid[x][y])

            
            if duplicatesExist(lis):
                return False
           

    return True


def duplicatesExist(row):

    lis = sorted(row)
    
    for i in range(0,len(lis)-1):
        if lis[i] == 0:
            pass
        else:
            if lis[i]==lis[i+1]:
                return True

    return False


def showGrid(grid,blanks):
    
    current_grid = grid
    for blank in blanks:
        current_grid[blank[0][0]][blank[0][1]]=blank[1]
    print("+-+-+-+-+-+-+-+-+-+")
    for i in range(0,len(current_grid)):

        for j in range(0,len(current_grid[i])):

            print("|",end="")
            print(current_grid[i][j],end="")

        print("|")
        print("+-+-+-+-+-+-+-+-+-+")

grid = [[2,0,3,0,8,0,0,0,0],
        [0,6,0,3,2,0,0,0,0],
        [5,0,0,0,0,6,0,0,0],
        [0,8,0,0,1,4,9,0,0],
        [7,1,0,6,0,9,0,4,8],
        [0,0,5,8,7,0,0,6,0],
        [0,0,0,5,0,0,0,0,1],
        [0,0,0,0,6,1,0,7,0],
        [0,0,0,0,3,0,8,0,4]
        ]

blanks = []

for i in range(0,len(grid)):
    for j in range(0,len(grid[i])):
        if grid[i][j] == 0:
            blanks.append([[i,j],0])

pointer = 0

print("incomplete:")
showGrid(grid,blanks)

while isComplete(blanks)==False:

    #showGrid(grid,blanks)
    if blanks[pointer][1]<9:
        blanks[pointer][1] += 1

        while blanks[pointer][1]<9 and isValid(grid,blanks)==False:
            blanks[pointer][1] = blanks[pointer][1]+1

        if isValid(grid,blanks):
            #print("forward")
            pointer += 1
        else:
            blanks[pointer][1] = 0
            pointer -= 1
            #print("back")
       
    else:
        blanks[pointer][1] = 0
        pointer -= 1
        #print("back")
          
print("complete:")
showGrid(grid,blanks)
        
        
        
    
        
        

