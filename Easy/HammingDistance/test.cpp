#include <iostream>
using namespace std;

class Solution {
public:
	int hammingDistance(int x, int y) {
		int w = x^y;
		int dist = 0;
		while (w) {
			dist ++;
			w &= w-1;
		}
		return dist;
	}
};

int main() {
	Solution sol;
	int hammingDist = sol.hammingDistance(1, 4);
	cout << "hamming distance is:" << hammingDist << endl;
}
