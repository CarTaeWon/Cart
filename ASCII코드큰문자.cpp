#include <iostream>
using namespace std;

int main()
{
	char arr[100];
	int len = 0;
	char max = 0;

	cin >> arr;

	while (arr[len] != '\0') {
		len++;		//for�� ���� �� �ʿ��� �ܾ� ����
	}
	for (int i = 0; i < len; i++) {
		if (max < arr[i]) {	//max�� ����� �ܾ�� arr[i]�� ũ��
			max = arr[i];	//max�� ���� �������ָ鼭 �� ū�� ã������ ��� ��
		}
	}
	cout << max << endl;

	return 0;
}