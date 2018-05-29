#include <iostream>
#include <iomanip>
#include <time.h>
using namespace std;

int random() { return rand() % 100; };

int main()
{
	int len = 10;
	int arr[10];
	int temp = 0;

	srand((unsigned)time(NULL));

	for (int i = 0; i < len; i++) {
		arr[i] = random();
	}
	for (int i = 0; i < len; i++) {
		cout << arr[i] << " ";
	}
	cout << endl;
	for (int i = 0; i < len - 1; i++) {
		for (int j = 0; j < len - 1; j++) {
			if (arr[j] > arr[j + 1]) {
				temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}
	for (int i = 0; i < len; i++) {
		cout << arr[i] << " ";
	}

	return 0;
}