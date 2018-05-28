#include <iostream>
#include <iomanip>
using namespace std;

struct point
{
	int xpos;
	int ypos;
};
struct circle
{
	double radius;
	struct point * center;
};
int main()
{
	struct point cen = { 2,7 };
	double rad = 5.5;
	struct circle ring = { rad, &cen };
	// ring.radius = rad
	cout << ring.radius << endl;
	cout << (ring.center)->xpos << setw(7) << (ring.center)->ypos << endl;
	// -> : 포인터 , xpos 주소 가리킴(xpos의 값 : 2),(ypos의 값 : 7)
	return 0;
}