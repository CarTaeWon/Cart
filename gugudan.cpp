#include <iostream>
using namespace std;
//3�� 9���� int �� �迭 ���� �� 2,3,4�� ���� ���
int main()
{
	int gugudan[3][9];

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 9; j++) {
			gugudan[i][j] = (i + 2)*(j + 1);
		}
	}
	for (int i = 0; i < 3; i++) {
		cout << "----------" << i + 2 << "��" << endl;
		for (int j = 0; j < 9; j++) {
			cout << i + 2 << " * " << j + 1 << " = " << gugudan[i][j] << endl;
		}
	}

	return 0;
}