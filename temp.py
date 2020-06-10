nm = input().split()

n = int(nm[0])

m = int(nm[1])

grid = []

for _ in range(n):
    grid_item = input()
    grid.append(grid_item)


def twoPluses(grid):
    Plus = [1]*2
    Except = [-1,-1]
    def multi(list):
        multi = 1
        for i in list:
            multi *= i
        return multi
    # Danh dau khoang da xet

    def flagStringrow(row, col, time):
        start = col-(time//2)
        end = col + (time//2)
        l = len(grid[row])
        grid[row] = grid[row].replace(
            grid[row], grid[row][0:start]+'-'*time+grid[row][end+1:l])

    def flagStringcol(row, col, time):
        back = row-1
        forw = row+1
        l = len(grid[row])
        grid[row] = grid[row].replace(
            grid[row], grid[row][0:col]+'|'+grid[row][col+1:l])
        time -= 1
        while True:
            if time <= 0:
                break
            grid[back] = grid[back].replace(
                grid[back], grid[back][0:col]+'|'+grid[back][col+1:l])
            grid[forw] = grid[forw].replace(
                grid[forw], grid[forw][0:col]+'|'+grid[forw][col+1:l])
            back -= 1
            forw += 1
            time -= 2
    # Tim khoang G doc nhieu nhat

    def colString(i, j, state):
        string = grid[i][j]
        
        back = i-1
        forw = i+1
        while True:
            if back < 0 or forw >= n or j == state:
                return string
            if grid[back][j] == 'G' and grid[forw][j] == 'G':
                grid[back][j].lower()
                grid[forw][j].lower()
                string += grid[back][j] + grid[forw][j]
                back -= 1
                forw += 1
            else:
                return string
        return string
    # Tim Khoang G nganh nhieu nhat

    def rowString(i, j, state):
        string = grid[i][j]

        back = j-1
        forw = j+1
        while True:
            if back < 0 or forw >= n or i == state:
                return string
            if grid[i][back] == 'G' and grid[i][forw] == 'G':
                grid[i][back].lower()
                grid[i][forw].lower()
                string += grid[i][back] + grid[i][forw]
                back -= 1
                forw += 1
            else:
                return string
        return string

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'G':
                #forwC,backC,stringCol = colString(i, j, Except[0])
                #forwR,backR,stringRow = rowString(i, j, Except[1])
                stringCol = len(colString(i,j,Except[1]))
                stringRow = len(rowString(i,j,Except[0]))
                if stringCol % 2 != 0 and stringRow % 2 != 0:
                    Sum = min(stringCol, stringRow)*2-1
                    index = Plus.index(min(Plus))
                    if Sum > min(Plus):
                        Plus[index] = Sum
                        #Except = [i,j]
                        #ExceptR = [forwR,backC]
                        # Danh dau khoang da xet
                        # de khong xet lai diem da xet
                        #flagStringcol(i, j, (Sum//2)+1)
                        #flagStringrow(i, j, (Sum//2)+1)
    Multi = multi(Plus)
    return Multi


result = twoPluses(grid)
print()
for i in range(len(grid)):
    print(grid[i])
print(result)
