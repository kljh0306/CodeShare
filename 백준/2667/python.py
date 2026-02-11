n = int(input())
m = [list(map(int, input())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0
res = []

def OOB(x, y):
    return 0<=x and x<n and 0<=y and y<n

def dfs(x, y):
    global cnt
    cnt += 1
    visited[x][y] = 1

    for i in range(4) :
        nx = x+dx[i]
        ny = y+dy[i]
        if OOB(nx, ny) and m[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(nx, ny)

for i in range(n) :
    for j in range(n) :
        if(m[i][j] == 1 and visited[i][j] == 0):
            cnt = 0
            dfs(i,j)
            res.append(cnt)

res.sort()
print(len(res))
for i in res:
    print(i)
