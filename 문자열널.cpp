#include <iostream>
using namespace std;

int main() {
	char str[50] = "I like C++ programming";
	cout << str << endl;
	str[8] = '\0';
	cout << str << endl;
	str[6] = '\0';
	cout << str << endl;
	str[2] = '\0';
	cout << str << endl;	//\0 �� ������ ���ڿ��� ������ ��
	return 0;
}