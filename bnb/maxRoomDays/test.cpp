#include<iostream>
#include<vector>
using namespace std;

int maxRoomDays(vector<int>& input) {
	if (input.size() <= 1) return input.empty()? 0 : input[0];
	vector<int> dp = {input[0], max(input[0],input[1])};
	for (int i = 2; i < input.size(); ++i) {
		dp.push_back(max(input[i] + dp[i-2], dp[i-1]));
	}
	return dp.back();
}

int main(int argc, const char* argv[]){
	vector<int> input1 {4, 9, 6};
	int res1 = maxRoomDays(input1);
	cout << "first test case:" << res1 << endl;

	vector<int> input2 {4, 10, 3, 1, 5};
	int res2 =  maxRoomDays(input2);
	cout << "second test case:" << res2 << endl;
}
