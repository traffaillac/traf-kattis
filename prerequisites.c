#include <stdio.h>
#include <string.h>

static char courses[10000];

int main() {
	int K, M;
	while (scanf("%d %d", &K, &M) == 2) {
		memset(courses, 0, sizeof(courses));
		for (int k = 0, i; k < K; k++) {
			scanf("%d", &i);
			courses[i] = 1;
		}
		int graduate = 1;
		for (int m = 0, R, C; m < M; m++) {
			scanf("%d %d", &C, &R);
			int taken = 0;
			for (int c = 0, i; c < C; c++) {
				scanf("%d", &i);
				taken += courses[i];
			}
			graduate &= taken >= R;
		}
		puts(graduate ? "yes" : "no");
	}
}
