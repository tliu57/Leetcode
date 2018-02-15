#include <iostream>
#include <vector>
using namespace std;

void getAllPossibleStrings(vector<string>& res, string s, int start, int end) {
	if (start == end) {
		res.push_back(s);
		return;
	}
	s[start] = toupper(s[start]);
	getAllPossibleStrings(res, s, start+1, end);

	s[start] = tolower(s[start]);
	getAllPossibleStrings(res, s, start+1, end);

}

vector<string> decodeString(string s) {
	vector<string> res;
	if (s.empty()) {
		return res;
	}
	int n = (int)s.size();
	getAllPossibleStrings(res, s, 0, n);

	return res;
}

int main(int argc, const char* argv[]){
        string test = "lala";
        vector<string> result = decodeString(test);
	for (auto str: result)	cout << "string:" << str << endl;

}

