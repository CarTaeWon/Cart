#include <iostream>
using namespace std;

int main()
{
	char arr[100];
	int len = 0;
	int temp = 0;

	cin >> arr;

	while (arr[len] != '\0') {
		len++;	//�Է��� ������ ����
	}
	for (int i = 0; i < len / 2; i++) {	
		temp = arr[i];	//���� temp�� ���� ������ ������ �� �ְ���
		arr[i] = arr[(len - i) - 1];	
		arr[(len - i) - 1] = temp;
	}
	cout << arr << endl;

	return 0;
}