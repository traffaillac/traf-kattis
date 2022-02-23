#include <stdio.h>

char str[1000001];

int main() {
	int i = 0;
	for (char c; (c = getchar()) != '\n'; ) {
		if (c != '<')
			str[i++] = c;
		else
			i--;
	}
	str[i] = 0;
	puts(str);
}
