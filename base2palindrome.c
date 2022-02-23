#include <stdio.h>

int main() {
	int M;
	scanf("%d", &M);
	int digits = 1;
	int mid = 0;
	while (--M) {
		if (__builtin_popcount(mid) >= (digits - 1) / 2)
			mid = 0, digits++;
		else mid++;
	}
	int num = 1 | 1 << (digits - 1) | mid << (digits / 2);
	for (int i = 0; i < (digits - 1) / 2; i++)
		num |= (mid >> i & 1) << ((digits - 1) / 2 - i);
	printf("%d\n", num);
}
