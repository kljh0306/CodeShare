m, n = map(int, input().split())

floor = [0] * 10
visited = [[0 for _ in range(21)] for _ in range(21)]
board = []
cnt = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(m) :
    tmp = list(map(int, input().split()))
    board.append(tmp)

def OOB(x, y) :
    return 0<=x and x<m and 0<=y and y<n

def dfs(x, y):
    global cnt
    cnt+=1
    visited[x][y] = 1
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if OOB(nx, ny) and board[x][y] == board[nx][ny] and visited[nx][ny] == 0 :
            dfs(nx,ny)


for i in range(m) :
    for j in range(n) :
        if board[i][j] != -1 and visited[i][j] == 0 :
            cnt = 0
            dfs(i, j)
            floor[board[i][j]] = max(floor[board[i][j]], cnt)

for i in range(10) :
    if floor[i] > 0:
        print(i,floor[i])
