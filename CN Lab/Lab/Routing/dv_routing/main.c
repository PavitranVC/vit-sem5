#include <stdio.h>
#include <stdbool.h>

#define MAX_NODES 20
#define INF 9999

typedef struct{
    int dist[MAX_NODES];
    int nextHop[MAX_NODES];
} RouteTable;

void initNetwork(RouteTable tables[], int n){
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            if(i==j){
                tables[i].dist[j]=0;
                tables[i].nextHop[j]=i;
            } else{
                tables[i].dist[j]=INF;
                tables[i].nextHop[j]=-1;
            }
        }
    }
}

void computeDVR(RouteTable tables[], int n){
    bool x;
    do{
        x=false;
        for(int i=1; i<=n; i++){
            for(int j=1; j<=n; j++){
                for(int k=1; k<=n; k++){
                    if(tables[i].dist[k]!=INF && tables[k].dist[j]!=INF){
                        if(tables[i].dist[j] > tables[i].dist[k] + tables[k].dist[j]){
                            tables[i].dist[j] = tables[i].dist[k] + tables[k].dist[j];
                            tables[i].nextHop[j] = tables[i].nextHop[k];
                            x=true;
                        }
                    }
                }
            }
        }
    } while(x);
}

void displayTables(RouteTable tables[], int n){
    for(int i=1; i<=n; i++){
        printf("Router %d:\n", i);
        printf("Destination\tCost\tNext Hop\n");
        for(int j=1; j<=n; j++){
            printf("%d\t\t%d\t", j, tables[i].dist[j]);
            if(tables[i].nextHop[j]==j){
                printf("-\n");
            } else{
                printf("%d\n", tables[i].nextHop[j]);
            }
        }
    }
}

int main(){
    int n, l;
    scanf("%d %d", &n, &l);

    RouteTable tables[MAX_NODES];
    initNetwork(tables, n);

    for(int i=0; i<l; i++){
        int u, v, cost;
        scanf("%d %d %d", &u, &v, &cost);
        tables[u].dist[v] = cost;
        tables[u].nextHop[v] = v;
        tables[v].dist[u] = cost;
        tables[v].nextHop[u] = u;
    }

    computeDVR(tables, n);
    displayTables(tables, n);

    return 0;
}
