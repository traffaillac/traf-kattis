#include <math.h>
#include <stdio.h>

typedef struct { int u, v; double w; } Edge;
static int C, R, c1, c2, A, B;
static int names[200];
static double dists[200];
static Edge edges[39800];

int find(int name) {
	for (int c = 0; c < C; c++) {
		if (names[c] == name)
			return c;
	}
	return 0;
}

int main() {
	while (scanf("%d", &C), C > 0) {
		for (int c = 0; c < C; c++)
			scanf("%s ", (char *)&names[c]);
		scanf("%d ", &R);
		for (int r = 0; r < R; r++) {
			scanf("%s %s %d:%d ", (char *)&c1, (char *)&c2, &A, &B);
			edges[r] = (Edge){find(c1), find(c2), log((double)B / (double)A)};
		}
		for (int c = 0; c < C; c++)
			dists[c] = 0.0;
		int updated = 1;
		for (int i = 0; updated && i < C; i++) {
			updated = 0;
			for (Edge *e = edges; e < edges + R; e++) {
				if (dists[e->u] + e->w > dists[e->v])
					dists[e->v] = dists[e->u] + e->w, updated = 1;
			}
		}
		puts(updated ? "Arbitrage" : "Ok");
	}
}
