#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
	vector<string> fullJustify(vector<string>& words, int maxWidth) {
		vector<string> res;
		for(int i = 0, currNumOfWords, currLen; i < words.size(); i += currNumOfWords) {
			for (currNumOfWords = currLen = 0; i + currNumOfWords < words.size() and currLen + currNumOfWords + words[i+currNumOfWords].size() <= maxWidth; currNumOfWords++) {
				currLen += words[i+currNumOfWords].size();
			}
			string tmp = words[i];
			for(int j = 0; j < currNumOfWords-1; j++) {
				if (i + currNumOfWords >= words.size()) tmp += " ";
				else tmp += string((maxWidth - currLen)/(currNumOfWords - 1) + (j < (maxWidth - currLen)% (currNumOfWords - 1)), ' ');
				tmp += words[i+j+1];
			}
			tmp += string(maxWidth-tmp.size(), ' ');
			res.push_back(tmp);
		}
		return res;
	}
};

int main(int argc, char* argv[]) {
	Solution sol;
	vector<string> words;
	words.push_back("This");
	words.push_back("is");
	words.push_back("an");
	words.push_back("example");
	words.push_back("of");
	words.push_back("text");
	words.push_back("justification.");
	int L = 16;
	vector<string> res = sol.fullJustify(words, L);
	for (int i = 0; i < res.size(); i++) {
		cout << res[i] << endl;
	}
	return 0;
}
