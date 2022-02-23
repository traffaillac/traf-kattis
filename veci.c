#include <math.h>
#include <stdio.h>
#include <string.h>

char counts1[10], counts2[10];

int main() {
	int X;
	scanf("%d", &X);
	int dig = log10(X) + 1;
	int max = pow(10, dig);
	for (int x = X; x > 0; x /= 10)
		counts1[x % 10]++;
	for (int x = X; ++x < max; ) {
		memset(counts2, 0, 10);
		for (int i = x; i > 0; i /= 10)
			counts2[i % 10]++;
		if (memcmp(counts1, counts2, 10) == 0) {
			printf("%d\n", x);
			return 0;
		}
	}
	puts("0");
	return 0;
}
