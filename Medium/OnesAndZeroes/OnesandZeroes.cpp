#include <iostream>
#include <queue>
#include <set>
#include <tuple>
#include <utility>
#include <vector>

using namespace std;


class Solution {
    public:
	int findMaxForm(vector<string>& strs, int m, int n) {
	    vector<vector<int>> memo(m+1, vector<int>(n+1, 0));
	    int numZeroes, numOnes;
	    int sumNumZeroes = 0, sumNumOnes = 0;

	    for (auto &s : strs) {
		numZeroes = 0; 
		numOnes = 0;
		// count number of zeroes and ones in current string
		for (auto c : s) {
		    if (c == '0')
			numZeroes++;
		    else if (c == '1')
			numOnes++;
		}
		sumNumZeroes += numZeroes;
		sumNumOnes += numOnes;

		for (int i = m; i >= numZeroes; i--) {
		    for (int j = n; j >= numOnes; j--) {
			memo[i][j] = max(memo[i][j], memo[i - numZeroes][j - numOnes] + 1);
		    }
		}

		
		cout << s << ":\n";
		for (int i = 0; i <= m; ++i) {
		    for (int j = 0; j <= n; ++j) {
			cout << memo[i][j] << " ";
		    }
		    cout << "\n";
		}
		cout << "\n";
		

	    }
	    return memo[m][n];
	}
};

int main() {
    Solution solver;
    vector<string> strs = {"10","0001","111001","1","0"};
    //vector<string> strs = {"10","0001","111001","1","0001","111001","0"};
    //vector<string> strs = {"0","0","1","1"};
    int m = 5, n = 3;
    cout << solver.findMaxForm(strs, m, n) << "\n";
    return 0;
}

