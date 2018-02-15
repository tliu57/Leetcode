#include <iostream>
#include <vector>
using namespace std;

class Vector2D {
private:
	vector<vector<int>> vec2d;
	int i;
	int j;
	int prev_i;
	int prev_j;

	void moveToNext() {
		while (i < vec2d.size()) {
			if (j < vec2d[i].size()) {
				break;
			}
			i += 1;
			j = 0;
		}
	}

public:
	Vector2D(vector<vector<int>>& input): vec2d(input), prev_i(-1), prev_j(-1), i(0), j(0) {}

	
	bool hasNext() {
		return i < vec2d.size();
	}
	
	int next() {
		if (hasNext()) {
			prev_i = i;
			prev_j = j;
			j++;
			moveToNext();
			//cout << "prev_i" << prev_i;
			cout << "prev_j:" << prev_j;
			return vec2d[prev_i][prev_j];
		}
		else return -1;
	}

	void remove() {
		if (prev_i != -1 && prev_j != -1) {
			vector<int> row = vec2d[prev_i];
			row.erase(row.begin() + prev_j);
			// for (auto idx = row.begin(); idx != row.end(); ++idx) cout << *idx << ' ';
			i = prev_i;
			j = prev_j;
			moveToNext();
			prev_i = -1;
			prev_j = -1;
		}
		else{
			return;
		}
	}
};

int main() {
	vector<vector<int>> vec2d;
	vec2d.push_back({1, 2});
	vec2d.push_back({3});
	vec2d.push_back({4, 5, 6});
	Vector2D i(vec2d);
	i.next();
	i.next();
	i.next();
	i.next();
	i.next();
	i.remove();
	//while (i.hasNext()) {
	//	cout << i.next();
	//}
}
