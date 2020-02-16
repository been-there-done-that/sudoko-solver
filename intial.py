
def create_grid(x):
    y = []
    for i in x:
        y.append([int(" ".join(j)) for j in i])
    return y

temp = ["530070000","600195000","098000060","800060003","400803001","700020006","060000280","060000280","000419005","000080079"]

grid = create_grid(temp)

def possible(y,x,n):
    global grid
    for i in range(0,9) :
        if grid[y][i] == n:
            return False
    for i in range(0,9) :
        if grid[i][x] == n:
            return False
        
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0,3) :
        for j in range(0,3) :
            if grid[y0 + i][x0 + j] == n :
                return False
    return True
