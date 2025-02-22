class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hash_map;

        for(string s: strs) {
            string sorted_s = s;
            sort(sorted_s.begin(), sorted_s.end());

            hash_map[sorted_s].push_back(s);
        }

        vector<vector<string>> res;
        for (const auto& pair: hash_map) {
            res.push_back(pair.second);
        }
        return res;
    }
};