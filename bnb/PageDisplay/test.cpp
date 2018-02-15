#include <iostream>
#include <vector>
#include <sstream>
#include <string>
using namespace std;

int main() {
	string line = "19 9 7.8 	Wuhan";
	stringstream ss(line);
	int hostId = 0, listingId = 0;
	float score = 0.0;
	string city = "";
	ss >> hostId >> listingId >> score >> city;
	cout << hostId << endl;
	cout << listingId << endl;
	cout << score << endl;
	cout << city << endl; 
}
