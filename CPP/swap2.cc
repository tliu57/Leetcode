#include <iostream>
using namespace std;

void swap(int *pa, int *pb) {
	int temp = *pa;
	*pa = *pb;
	*pb = temp;
}

int main() {
	int a = 3;
	int b = 5;
	swap(a, b);
	cout << "After swapping a is: " << a << "b is:" << b;
	return 0;
}
