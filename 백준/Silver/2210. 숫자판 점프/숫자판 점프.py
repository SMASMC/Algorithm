graph = []
num_list = []

for i in range(5):
    graph.append(list(map(int,input().split())))

def dfs(graph,ans,x,y):
    if len(ans) == 6:
        if ans not in num_list:
            num_list.append(ans)
        return

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(graph,ans + str(graph[nx][ny]),nx,ny)

for i in range(5):
    for j in range(5):
        dfs(graph,'',i,j)
        
print(len(num_list))