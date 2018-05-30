#include <iostream>
using namespace std;
//3행 9열인 int 형 배열 선언 후 2,3,4단 저장 출력
int main()
{
	int gugudan[3][9];

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 9; j++) {
			gugudan[i][j] = (i + 2)*(j + 1);
		}
	}
	for (int i = 0; i < 3; i++) {
		cout << "----------" << i + 2 << "단" << endl;
		for (int j = 0; j < 9; j++) {
			cout << i + 2 << " * " << j + 1 << " = " << gugudan[i][j] << endl;
		}
	}

	return 0;
}