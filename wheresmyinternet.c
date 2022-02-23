#include <stdio.h>
#include <string.h>

static inline int min(int a, int b) { return a < b ? a : b; }
static inline int max(int a, int b) { return a > b ? a : b; }

/* Manage elements in sets (begin with a -1 initialised array). */
static int  Set_find(int* set, int i) { return (set[i] < 0) ? i : (set[i] = Set_find(set, set[i])); }
static int  Set_test(int* set, int i, int j) { return (Set_find(set, i) == Set_find(set, j)); }
static int  Set_card(int* set, int i) { return -set[Set_find(set, i)]; }
static void Set_union(int* set, int i, int j) {
	int a = Set_find(set, i), b = Set_find(set, j), c;
	if (a != b) {
		if (set[a] > set[b])
			c = a, a = b, b = c;
		set[a] += set[b], set[b] = a;
	}
}

int main() {
	int N, M;
	scanf("%d %d", &N, &M);
	int set[N];
	memset(set, -1, sizeof(set));
	for (int m = 0, a, b; m < M; m++) {
		scanf("%d %d", &a, &b);
		Set_union(set, a - 1, b - 1);
	}
	int connected = 1;
	for (int n = 1; n < N; n++) {
		if (!Set_test(set, 0, n))
			printf("%d\n", n + 1), connected = 0;
	}
	if (connected)
		puts("Connected");
	return 0;
}
