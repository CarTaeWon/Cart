#include <iostream>
using namespace std;

int main()
{
	int arr[6];
	int sum = 0;

	for (int i = 0; i < 6; i++) {
		cin >> arr[i];
	}
	for (int i = 0; i < 6; i++) {
		sum += arr[i];
	}

	cout << "�հ� : " << sum << endl;

	return 0;
}