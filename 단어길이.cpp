#include <iostream>
using namespace std;

int main()
{
	char arr[100];
	int len = 0;

	cin >> arr;

	while (arr[len] != '\0') {		//���ڿ��� ���� \0���ڰ� ���� ������ �ݺ�
		len++;						
	}
	cout << len << endl;

	return 0;
}