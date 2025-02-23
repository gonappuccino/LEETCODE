class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = 0;

        for(int num: nums) {
            //XOR
            // a ^ a = 0
            // a ^ 0 = a
            result ^= num;
        }

        return result;
    }
};