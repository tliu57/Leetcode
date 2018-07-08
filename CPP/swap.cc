#include <iostream>

using namespace std;

void swap(int& a, int& b) {
	int aVal = a;
	a = b;
	b = aVal;
}

int main() {
	int a = 3;
	int b = 5;
	swap(a, b);
	cout << "After swapping, a:" << a << " b:" << b;
}
