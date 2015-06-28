#include <vector>
#include <iostream>
#include <cmath>
#include <cstddef>
using namespace std;

class Solution {
	public:
		vector<int> grayCode(int n) {
			vector <int> res;
			if (n < 0)	return res;
			if (n == 0) {
				res.push_back(0);
				return res;
			}
			res = grayCode(n-1);
			size_t size = res.size();
			unsigned int exp = n > 1? pow(2, n-1) : 1;
			for(long long i = size - 1; i >= 0 ; i--) {
				res.push_back(res[i]+exp);
			}
			return res;
		}
		

};

int main(int argc, char **argv) {
	Solution solver;
	int n = argc > 1? atoi(argv[1]) : 2;
	vector<int> res = solver.grayCode(n);
	for(size_t i = 0; i < res.size(); i++)
		cout << res[i] << " ";
	cout << "\n";
}
