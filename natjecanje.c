#include <stdio.h>

int main() {
	int N, S, R;
	scanf("%d %d %d", &N, &S, &R);
	int damaged = 0;
	for (int s = 0, i; s < S; s++) {
		scanf("%d", &i);
		damaged |= 1 << i;
	}
	int reserve = 0;
	for (int r = 0, i; r < R; r++) {
		scanf("%d", &i);
		if (damaged & 1 << i)
			damaged ^= 1 << i;
		else
			reserve |= 1 << i;
	}
	for (; reserve; reserve &= reserve - 1) {
		int i = __builtin_ctz(reserve);
		if (damaged & 1 << (i - 1))
			damaged ^= 1 << (i - 1);
		else if (damaged & 1 << (i + 1))
			damaged ^= 1 << (i + 1);
	}
	printf("%d\n", __builtin_popcount(damaged));
}
