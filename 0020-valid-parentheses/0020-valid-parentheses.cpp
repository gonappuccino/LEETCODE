class Solution {
public:
    bool isValid(string s) {
        vector<char> freq;
        for(int i = 0; i < s.size(); i++) {
            if (freq.size() != 0 && freq.back() == '(' && s[i] == ')') {
                freq.pop_back();
            }
            else if (freq.size() != 0 && freq.back() == '[' && s[i] == ']') {
                freq.pop_back();
            }
            else if (freq.size() != 0 && freq.back() == '{' && s[i] == '}') {
                freq.pop_back();
            }
            else {
                freq.push_back(s[i]);
            }    
            
        }
        if (freq.size() == 0) {
            return true;
        }
        return false;

    }
};