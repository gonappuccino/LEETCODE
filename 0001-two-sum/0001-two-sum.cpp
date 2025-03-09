class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash;

        for(int i = 0; i < size(nums); i++) {
            int complement = target - nums[i];
            if(hash.find(complement) != hash.end()) {
                return {hash[complement],i};
            }
            hash[nums[i]] = i; 
        }
        return {};
    }
};