#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int T, n;
struct { int class; char name[32]; } people[100];
char str[7];

static inline int comp(const void *a, const void *b) {
	int i = *(int *)a, j = *(int *)b;
	return i != j ? j - i : strcmp(a + 4, b + 4);
}

int main() {
	scanf("%d", &T);
	while (T-- > 0) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf(" %[^:]: ", people[i].name);
			int mult = 1, class = 0;
			do {
				scanf("%[^- ]", str);
				class += mult * ((strcmp(str, "upper") == 0) - (strcmp(str, "lower") == 0));
				mult *= 3;
			} while (getchar() == '-');
			class *= 59049 / mult;
			scanf(" %*s");
			people[i].class = class;
		}
		qsort(people, n, sizeof(*people), comp);
		for (int i = 0; i < n; i++)
			puts(people[i].name);
		puts("==============================");
	}
	return 0;
}
