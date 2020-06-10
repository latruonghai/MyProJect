nm = input().split()

n = int(nm[0])

m = int(nm[1])

grid = []

for _ in range(n):
    grid_item = input()
    grid.append(grid_item)


def twoPluses(grid):
    lc = len(grid[0])
    lr = len(grid)
    Plus = [1]*2
    Except = [0, 0]

    def multi(list):
        multi = 1
        for i in list:
            multi *= i
        return multi

    # Tim khoang G doc nhieu nhat

    def colString(i, j):
        string = grid[i][j]
        back = i-1
        forw = i+1
        while True:
            if back < 0 or forw >= lr:
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

    def rowString(i, j):
        string = grid[i][j]
        Except = []
        back = j-1
        forw = j+1
        while True:
            if back < 0 or forw >= lc:
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

    for i in range(lr):
        for j in range(lc):
            if grid[i][j] == 'G':
                stringCol = len(colString(i, j))
                stringRow = len(rowString(i, j))
                if stringCol % 2 != 0 and stringRow % 2 != 0:
                    Sum = min(stringCol, stringRow)*2-1
                    index = Plus.index(min(Plus))
                    if Sum > min(Plus):
                        Plus[index] = Sum
                        # Danh dau khoang da xet
                        # de khong xet lai diem da xet
                        grid[i] = grid[i].replace(
                            grid[i], grid[i][0:j]+'b'+grid[i][j+1:len(grid[1])])
    Multi = multi(Plus)
    return Multi


result = twoPluses(grid)
print()
for i in range(len(grid)):
    print(grid[i])
print(result)
