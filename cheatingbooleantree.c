#include <stdio.h>
#include <string.h>

static inline int min(int a, int b) { return a < b ? a : b; }
static inline int max(int a, int b) { return a > b ? a : b; }

static char G[10000], C[10000], I[10000];
static short cost[10000][2];

int main() {
	int N;
	scanf("%d", &N);
	for (int n = 1; n <= N; n++) {
		int M, V;
		scanf("%d %d", &M, &V);
		for (int m = 0; m < (M - 1) / 2; m++)
			scanf("%hhd %hhd", &G[m], &C[m]);
		for (int m = (M - 1) / 2; m < M; m++) {
			scanf("%hhd", &I[m]);
			cost[m][I[m]] = 0;
			cost[m][1 - I[m]] = 10000;
		}
		
		for (int m = (M - 3) / 2; m >= 0; m--) {
			int l = m * 2 + 1;
			int r = m * 2 + 2;
			I[m] = G[m] ? I[l] & I[r] : I[l] | I[r];
			int costA0 = min(cost[l][0], cost[r][0]);
			int costA1 = cost[l][1] + cost[r][1];
			int costO0 = cost[l][0] + cost[r][0];
			int costO1 = min(cost[l][1], cost[r][1]);
			cost[m][0] = C[m] ? min(costA0 + 1 - G[m], costO0 + G[m]) : G[m] ? costA0 : costO0;
			cost[m][1] = C[m] ? min(costA1 + 1 - G[m], costO1 + G[m]) : G[m] ? costA1 : costO1;
		}
		printf(cost[0][V] < 10000 ? "Case #%d: %d\n" : "Case #%d: IMPOSSIBLE\n", n, cost[0][V]);
	}
}
