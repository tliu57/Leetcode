#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
	vector<string> fizzBuzz(int n) {
		vector<string> ret_vec(n);
		for(int i = 1; i <= n ; i++) {
			if(i%3 == 0){
				ret_vec[i-1] += string("Fizz");
			}
			if(i%5 == 0) {
				ret_vec[i-1] += string("Buzz");
			}
			// note: this will append anything that makes i%5 != 0 to ret_vec!!
			//else {
			//	ret_vec[i-1] += to_string(i);
			//}
			if (ret_vec[i-1] == "") {
				ret_vec[i-1] += to_string(i);
			} 
		}
		return ret_vec;
	}
};

int main(int argc, char* argv[]) {
	int n = 15;
	vector<string> result;
	Solution mySol; 
	result = mySol.fizzBuzz(n);
	for(int i = 0; i < n; i++){
		cout << i+1 << "->" <<result[i] << endl;
	}
	return 0;
}
