#include <stdio.h>
#include <string.h>

static const char a[] = {
	
};

int main() {
	const char *qwerty = "`1234567890-QWERTYUIOP[]ASDFGHJKL;ZXCVBNM,. \n";
	const char *wertyu = "1234567890-=WERTYUIOP[]\\SDFGHJKL;'XCVBNM,./ \n";
	int c;
	while ((c = getchar()) >= 0) {
		putchar(qwerty[strchr(wertyu, c) - wertyu]);
	}
	return 0;
}
