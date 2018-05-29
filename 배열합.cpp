#include <iostream>
using namespace std;
//배열에 있는 값의 합
int main()
{
	int sum = 0;
	int a[5] = { 5,6,7,8,9 };

	for (int i = 0; i < 5; i++) {
		sum += a[i];
	}
	cout << "총합 : " << sum << endl;

	return 0;
}