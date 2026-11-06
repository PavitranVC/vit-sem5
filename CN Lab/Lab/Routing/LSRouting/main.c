#include <stdio.h>
#include <stdbool.h>

#define MAX_NODES 20
#define INF 9999

void printPath(int parent[], int j){
    if(parent[j]==-1){
        printf("%d", j);
        return;
    }
    printPath(parent, parent[j]);
    printf(" -> %d", j);
}

void computeLSR(int costMat[MAX_NODES][MAX_NODES], int n, int src){
    int dist[MAX_NODES];
    bool visited[MAX_NODES];
    int parent[MAX_NODES];

    for(int i=0; i<n; i++){
        dist[i] = INF;
        visited[i] = false;
        parent[i] = -1;
    }

    dist[src] = 0;

    for(int count=0; count<n-1; count++){
        int u = -1;
        int min = INF;

        for(int i=0; i<n; i++){
            if(!visited[i] && dist[i] < min){
                min = dist[i];
                u = i;
            }
        }

        if(u==-1) break;
        visited[u] = true;

        for(int v=0; v<n; v++){
            if(!visited[v] && costMat[u][v] != 0 && dist[u] != INF && dist[u] + costMat[u][v] < dist[v]){
                dist[v] = dist[u] + costMat[u][v];
                parent[v] = u;
            }
        }
    }

    printf("Routing Table for Router %d\n", src);
    printf("Destination\tCost\tPath\n");
    for(int i=0; i<n; i++){
        printf("%d\t\t%d\t", i, dist[i]);
        printPath(parent, i);
        printf("\n");
    }
}

int main(){
    int n, src;
    int costMat[MAX_NODES][MAX_NODES];

    printf("Enter number of routers: ");
    scanf("%d", &n);

    printf("Enter the cost matrix:\n");
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            scanf("%d", &costMat[i][j]);
        }
    }

    printf("Enter source router: ");
    scanf("%d", &src);

    computeLSR(costMat, n, src);

    return 0;
}
