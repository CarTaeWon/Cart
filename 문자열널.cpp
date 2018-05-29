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
	cout << str << endl;	//\0 가 나오면 문자열의 끝으로 앎
	return 0;
}