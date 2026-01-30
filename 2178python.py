n, m = map(int,input().split())
board = []
q = []
visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def OOB(x, y) :
    return 0<=x and x<n and 0<=y and y<m

for i in range(n) :
    tmp = list(map(int, input()))
    board.append(tmp)

q.append([1, 0, 0])
while len(q) != 0 :
    now = q[0]
    q.pop(0)
    if now[1] == n-1 and now[2] == m-1 :
        print(now[0])
        break

    for i in range(4) :
        now_x = now[1] + dx[i]
        now_y = now[2] + dy[i]
        if OOB(now_x, now_y) and board[now_x][now_y] == 1 and visited[now_x][now_y] ==0 :
            q.append([now[0]+1,now_x, now_y])
            visited[now_x][now_y] = 1

