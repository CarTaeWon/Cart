#include <iostream>
using namespace std;
//�迭�� �ִ� ���� ��
int main()
{
	int sum = 0;
	int a[5] = { 5,6,7,8,9 };

	for (int i = 0; i < 5; i++) {
		sum += a[i];
	}
	cout << "���� : " << sum << endl;

	return 0;
}