#include <iostream>
using namespace std;

int main()
{
	char arr[100];
	int len = 0;

	cin >> arr;

	while (arr[len] != '\0') {		//문자열의 끝인 \0문자가 나올 때까지 반복
		len++;						
	}
	cout << len << endl;

	return 0;
}