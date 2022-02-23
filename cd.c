#include <stdio.h>

int catalog[1000001];

int main() {
	int N, M;
	while (scanf("%d %d", &N, &M), N > 0 || M > 0) {
		for (int n = 0; n < N; n++)
			scanf("%d", &catalog[n]);
		int sum = 0;
		for (int m = 0, n = 0, cd; m < M; m++) {
			scanf("%d", &cd);
			while (n < N && catalog[n] < cd)
				n++;
			sum += cd == catalog[n];
		}
		printf("%d\n", sum);
	}
}
