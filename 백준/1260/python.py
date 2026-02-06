queue = []
adj = [[0 for _ in range(1001)] for _ in range(1001)]
visited_dfs = [0 for _ in range(1001)]
visited_bfs = [0 for _ in range(1001)]

n, m, v = map(int, input().split())
for i in range(m) :
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1

def dfs(now) :
    visited_dfs[now] = 1
    print(now, end=' ')
    for i in range(1, n+1) :
        if adj[now][i] == 1 and visited_dfs[i] == 0:
            dfs(i)
    return

def bfs(start) :
    queue.append(start)
    visited_bfs[start] = 1
    while len(queue) != 0:
        now = queue.pop(0)
        print(now, end=' ')
        for i in range(1, n+1) :
            if adj[now][i] == 1 and visited_bfs[i] == 0:
                visited_bfs[i] = 1
                queue.append(i)

dfs(v)     
print()
bfs(v)
