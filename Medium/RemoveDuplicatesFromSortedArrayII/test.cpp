#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
	int removeDuplicates(vector<int>& nums) {
		int i = 0;
		for (int n: nums) {
			if (i < 2 || n > nums[i-2])
				nums[i++] = n;
		}
		return i;
	}
};

int main()
{
	int nums[] = {1,1,1,2,2,3};
	vector<int> nums2(nums, nums+sizeof(nums)/sizeof(int));
	Solution sol;
	int length = sol.removeDuplicates(nums2);
	cout << "length is:" << length << endl;
}
