#include <iostream>
#include <vector>
using namespace std;

class Vector2D {
	vector<vector<int>>::iterator i, iEnd;
	int j = 0;

public:
	Vector2D(vector<vector<int>>& vec2d) {
		i = vec2d.begin();
		iEnd = vec2d.end();
	}

	int next() {
		if (hasNext()) {
			return (*i)[j++];
		}
		else return -1;
	}

	bool hasNext() {
		if (i != iEnd and j == (*i).size()) {
			i++;
			j = 0;
		}
		return i != iEnd;	
	}
	iterator remove() {
		(*i).erase(j);
	}
};

int main() {
	vector<vector<int>> vec2d;
	vec2d.push_back({1,2});
	vec2d.push_back({3});
	vec2d.push_back({4, 5, 6});
	Vector2D j(vec2d);
	vector<vector<int>> vec2dWithEmpty;
	vec2dWithEmpty.push_back({1});
	vec2dWithEmpty.push_back({});
	Vector2D i(vec2dWithEmpty);
	while (i.hasNext()) cout << i.next();
}
