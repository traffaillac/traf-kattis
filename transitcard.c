#include <stdio.h>

static inline int min(int a, int b) { return a < b ? a : b; }

int main() {
	short ppd[100];
	int days[99];
	int prices[1000001];
	int first[5000];
	int last[5000];
	int cost[5000];
	int L, T, N;
	scanf("%d", &L);
	for (int l = 0; l < L; l++)
		scanf("%hd", &ppd[l]);
	for (int l = 0; l < L - 1; l++)
		scanf("%d", &days[l]);
	days[L - 1] = 1000000;
	scanf("%d %d", &T, &N);
	prices[0] = 0;
	for (int t = 1, p = 0, l = 0, d = days[0]; t <= T; t++) {
		prices[t] = p += ppd[l];
		if (--d == 0)
			d = days[++l];
	}
	
	for (int n = 0; n < N; n++) {
		scanf("%d %d", &first[n], &last[n]);
		int best = prices[first[n] - 1];
		for (int i = 0; i < n; i++) {
			best = min(best, cost[i] + prices[first[n] - last[i] - 1]);
		}
		cost[n] = best;
	}
	int best = prices[T];
	for (int i = 0; i < N; i++) {
		best = min(best, cost[i] + prices[T - last[i]]);
	}
	printf("%d\n", best);
}
