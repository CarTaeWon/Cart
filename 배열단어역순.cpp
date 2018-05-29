#include <iostream>
using namespace std;

int main()
{
	char arr[100];
	int len = 0;
	int temp = 0;

	cin >> arr;

	while (arr[len] != '\0') {
		len++;	//입력한 문자의 길이
	}
	for (int i = 0; i < len / 2; i++) {	
		temp = arr[i];	//변수 temp에 값을 대입해 스왑할 수 있게함
		arr[i] = arr[(len - i) - 1];	
		arr[(len - i) - 1] = temp;
	}
	cout << arr << endl;

	return 0;
}