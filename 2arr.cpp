#include <iostream>
using namespace std;

int main()
{
	int arr1[3][3] = { { 1,2,3 },{ 4,5,6 },{ 7,8,9 } };
	int arr2[3][3] = { { 1 },{ 4,5 },{ 7,8,9 } };
	int arr3[3][3] = { 1,2,3,4,5,6,7 };

	for (int i = 0; i < 3; i++) {			//123
		for (int j = 0; j < 3; j++) {		//456
			cout << arr1[i][j] << " ";		//789
		}
		cout << endl;
	}
	for (int i = 0; i < 3; i++) {			//100
		for (int j = 0; j < 3; j++) {		//450
			cout << arr1[i][j] << " ";		//789
		}
		cout << endl;
	}
	for (int i = 0; i < 3; i++) {			//123
		for (int j = 0; j < 3; j++) {		//456
			cout << arr1[i][j] << " ";		//789
		}
		cout << endl;
	}

	return 0;
}