import random


DIRECTIONS = {
    "S" : [0,1],
    "E" : [1,0],
    "SE": [1,1]
}

def generate(words, size):
    grid = [[" " for _ in range(size)] for _ in range(size)];
    allLetters = ""

    sortedWords = sortLength(words)

    for w in sortedWords:
        i = 0
        for char in w:
            if char not in allLetters:
                allLetters += char

        startCords = [None, None]
        finalDirection = [None, None]
        
        valid = False
        while i < 10000 and valid == False:
            direction, vector = random.choice(list(DIRECTIONS.items()))
            nextRow, nextCol = random.randint(0, size-1), random.randint(0, size-1)
            placed = 0
            while (nextRow < size and nextCol < size):
                if(placed == len(w)):
                    startCords = [nextRow - (vector[0]*placed), nextCol - (vector[1]*placed)]
                    finalDirection = vector
                    valid = True
                    break
                if(grid[nextRow][nextCol] == " " or grid[nextRow][nextCol] == w[placed]):
                    nextRow += vector[0]
                    nextCol += vector[1]
                    placed+=1
                else:
                    break
            i += 1
        if(valid):
            grid = place(w, vector, grid, startCords)

    grid = gridFill(grid, allLetters)

    for rows in grid:
        print(rows)
    print(validate(grid,words))

def gridFill(grid, letters):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] == " "):
                grid[i][j] = letters[random.randint(0, len(letters)-1)]
    return grid

def sortLength(words):
    sorted = [""]

    for w in words:
        i = 0
        while(len(w) < len(sorted[i]) and i < len(sorted)):
            i += 1
        sorted.insert(i,w)

    return sorted

def place(word, direction, grid, start):

    for char in word:
        grid[start[0]][start[1]] = char
        start[0] = start[0]+direction[0]
        start[1] = start[1]+direction[1]


    return grid

def validate(grid, words):
    for w in words:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for direction, vector in DIRECTIONS.items():
                    startRow = i
                    startCol = j
                    if(startRow==len(grid) and startCol == len(grid[0])):
                        return False
                    for char in w:
                        if grid[startRow][startCol] == char:
                            startRow += vector[0]
                            startCol += vector[1]



    return True

        