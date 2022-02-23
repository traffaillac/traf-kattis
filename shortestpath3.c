#include <limits.h>
#include <stdio.h>

typedef struct { short u, v, w; } Edge;
static int N, M, Q, S;
static int dists[1000];
static Edge edges[5000];

int main() {
	while (scanf("%d%d%d%d", &N, &M, &Q, &S), N > 0) {
		for (int m = 0; m < M; m++)
			scanf("%hd%hd%hd", &edges[m].u, &edges[m].v, &edges[m].w);
		for (int n = 0; n < N; n++)
			dists[n] = INT_MAX;
		dists[S] = 0;
		int updated = 1;
		for (int i = 0; updated && i < N - 1; i++) {
			updated = 0;
			for (Edge *e = edges; e < edges + M; e++) {
				if (dists[e->u] != INT_MAX && dists[e->u] + e->w < dists[e->v]) {
					dists[e->v] = dists[e->u] + e->w, updated = 1;
				}
			}
		}
		if (updated) {
			for (int i = 0; updated && i < N - 1; i++) {
				updated = 0;
				for (Edge *e = edges; e < edges + M; e++) {
					if (dists[e->u] == INT_MIN || (dists[e->u] != INT_MAX && dists[e->u] + e->w < dists[e->v]))
						dists[e->v] = INT_MIN, updated = 1;
				}
			}
		}
		for (int q = 0, i; q < Q; q++) {
			scanf("%d", &i);
			printf(dists[i] == INT_MIN ? "-Infinity\n" : dists[i] == INT_MAX ? "Impossible\n" : "%d\n", dists[i]);
		}
		putchar('\n');
	}
}
