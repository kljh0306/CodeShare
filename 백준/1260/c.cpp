#include<stdio.h>
#include<string.h>
#include<queue>
using namespace std;
bool adj[1001][1001], visited[1001];
int n, m;

void dfs(int v)
{
    visited[v] = 1;
    printf("%d ", v);
    for(int i=1;i<=n;i++)
    {
        if(adj[v][i]&&!visited[i])
        {
            dfs(i);
        }
    }
    return;
}

int main()
{
    int v;
    scanf("%d %d %d", &n, &m, &v);
    for(int i=1;i<=m;i++)
    {
        int u, v;
        scanf("%d %d", &u, &v);
        adj[u][v] = adj[v][u] = 1;
    }
    dfs(v);

    //bfs
    printf("\n");
    memset(visited, 0, sizeof(visited));
    queue<int> q;
    q.push(v);
    visited[v]=1;
    while (!q.empty())
    {
        int cur = q.front(); q.pop();
        printf("%d ", cur);
        for(int i=1;i<=n;i++)
        {
            if(adj[cur][i]&&!visited[i])
            {
                visited[i]=1;
                q.push(i);
            }
        }
    }
}
