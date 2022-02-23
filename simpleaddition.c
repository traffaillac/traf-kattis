#include <stdio.h>
#include <string.h>

char str1[10002], str2[10002], str3[10002];

int main() {
	gets(str1);
	gets(str2);
	int i3 = 10001, carry = 0;
	for (int i1 = strlen(str1) - 1, i2 = strlen(str2) - 1; i1 >= 0 || i2 >= 0; i1--, i2--, i3--) {
		int digit1 = (i1 >= 0) ? str1[i1] - '0' : 0;
		int digit2 = (i2 >= 0) ? str2[i2] - '0' : 0;
		int digit3 = digit1 + digit2 + carry;
		str3[i3] = '0' + digit3 % 10;
		carry = digit3 / 10;
	}
	str3[i3] = '0' + carry;
	puts(str3 + i3 + (str3[i3] == '0'));
}
