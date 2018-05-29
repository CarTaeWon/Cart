#include <iostream>
using namespace std;

int main()
{
	char arr[100];
	int len = 0;
	char max = 0;

	cin >> arr;

	while (arr[len] != '\0') {
		len++;		//for문 돌릴 때 필요한 단어 길이
	}
	for (int i = 0; i < len; i++) {
		if (max < arr[i]) {	//max에 저장된 단어보다 arr[i]가 크면
			max = arr[i];	//max에 값을 대입해주면서 더 큰걸 찾기위해 계속 비교
		}
	}
	cout << max << endl;

	return 0;
}