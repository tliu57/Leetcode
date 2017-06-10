#include <vector>
#include <unordered_map>
#include <iostream>
using namespace std;

class Solution {
public:
	vector<vector< int > > palindromePairs(vector<string>& words) {
		unordered_map<string, int> dict;
		vector<vector<int> > res;
		for(int i = 0; i < words.size(); i++) {
			string key = words[i];
			reverse(key.begin(), key.end());
			dict[key] = i;
		}

		for (int i = 0; i < words.size(); i++) {
			for (int j = 0; j < words[i].size(); j++) {
				string left = words[i].substr(0, j);
				string right = words[i].substr(j, words[i].size()-j);
				if(isPalindrome(left) && dict[right] != i) {
					vector<int> temp_vec = {dict[right], i};
					res.push_back(temp_vec);
				}
				if(isPalindrome(right) && dict[left]!= i) {
					vector<int> temp_vec = {i, dict[left]};
					res.push_back(temp_vec);
				}
			}
		}
		return res;
	}

	bool isPalindrome(string str) {
		int i = 0;
		int j = str.size()-1;
		while (i < j) {
			if(str[i++] != str[j--]) return false;
		}
		return true;
	}
};

int main(int argc, char* argv[]) {
	Solution sol;
	vector<string> words;
	words.push_back("abcd");
	words.push_back("dcba");
	words.push_back("lls");
	words.push_back("s");
	words.push_back("sssll");
	vector<vector<int> > result = sol.palindromePairs(words);
	for(int i = 0; i < result.size(); i++) {
		cout << "[" ;
		for(int j = 0; j < result[i].size(); j++) {
			cout << result[i][j];
		}
		cout << "]" << endl;
	}
}
