#include <limits.h>
#include <stdio.h>
#include <string.h>

static struct { long long value, steps; } table[7919];

static void insert(long long v, long long s) {
	int i = (unsigned long long)v % 7919;
	while (table[i].value != 0)
		i = i < 952 ? i + 1 : 0;
	table[i].value = v;
	table[i].steps = s;
}

static int find(long long v) {
	int i = (unsigned long long)v % 7919;
	while (table[i].value != 0) {
		if (table[i].value == v)
			return table[i].steps;
		i = i < 952 ? i + 1 : 0;
	}
	return INT_MIN;
}

int main() {
	int A, B;
	while (scanf("%d %d", &A, &B) == 2 && A > 0) {
		//printf("A=%d, B=%d\n", A, B);
		memset(table, 0, sizeof(table));
		insert(A, 0);
		for (long long a = A, Sa = 1; a > 1; Sa++) {
			if (a & 1)
				a = a * 3 + 1;
			else
				a >>= 1;
			insert(a, Sa);
		}
		for (long long b = B, Sb = 0; ; Sb++) {
			int Sa = find(b);
			if (Sa != INT_MIN) {
				printf("%d needs %d steps, %d needs %d steps, they meet at %lld\n", A, Sa, B, (int)Sb, b);
				break;
			}
			if (b & 1)
				b = b * 3 + 1;
			else
				b >>= 1;
		}
	}
	return 0;
}
