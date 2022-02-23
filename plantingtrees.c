#include <stdio.h>
#include <stdlib.h>

static int max(int a, int b) { return a > b ? a : b; }
static int comp(const void *a, const void *b) { return *(int *)b - *(int *)a; }

static int days[100000];

int main() {
	int N;
	scanf("%d", &N);
	for (int n = 0; n < N; n++)
		scanf("%d", &days[n]);
	qsort(days, N, sizeof(*days), comp);
	int earliest = 0;
	for (int n = 0; n < N; n++)
		earliest = max(earliest, days[n] + n);
	printf("%d\n", earliest + 2);
}
