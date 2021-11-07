#include <stdio.h>
#include <string.h>

/* Manage elements in sets (begin with a -1 initialised array). */
static int  Set_find(int* set, int i) { return (set[i] < 0) ? i : (set[i] = Set_find(set, set[i])); }
static int  Set_test(int* set, int i, int j) { return (Set_find(set, i) == Set_find(set, j)); }
static int  Set_card(int* set, int i) { return -set[Set_find(set, i)]; }
static void Set_union(int* set, int i, int j) {
	int a = Set_find(set, i), b = Set_find(set, j), c;
	if (a != b) {
		if (set[a] < set[b])
			c = a, a = b, b = c;
		set[a] += set[b], set[b] = a;
	}
}

int main() {
	int set[1000000];
	int n, q;
	scanf("%d %d\n", &n, &q);
	memset(set, -1, n * sizeof(*set));
	for (int i = 0, a, b, c; i < q; i++) {
		c = getchar();
		if (c == 't') {
			scanf(" %d %d\n", &a, &b);
			Set_union(set, a-1, b-1);
		} else {
			scanf(" %d\n", &a);
			printf("%d\n", Set_card(set, a-1));
		}
	}
}
