#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static inline int min(int a, int b) { return a < b ? a : b; }
static inline int max(int a, int b) { return a > b ? a : b; }

int main() {
	int k, n;
	while (scanf("%d%d", &k, &n) == 2) {
		double ratios[10] = {1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0}, old[10];
		for (int i = 0; i < n - 1; i++) {
			memcpy(old, ratios, sizeof(ratios));
			for (int j = 0; j <= k; j++) {
				double sum = 0.0;
				for (int l = max(j - 1, 0); l <= min(j + 1, k); l++)
					sum += old[l];
				ratios[j] = sum / (k + 1);
			}
		}
		double sum = 0.0;
		for (int i = 0; i <= k; i++)
			sum += ratios[i];
		printf("%.9f\n", sum * 100.0 / (k + 1));
	}
	return 0;
}
