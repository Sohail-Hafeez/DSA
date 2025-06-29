class Solution {
public:
    string countAndSay(int n) {
        if(n == 1) {
            return "1";
        } else if(n == 2) {
            return "11";
        }

        int count = 1;
        bool check = false;
        string s = "11";
        string str = "";
        n = n - 2;

        while(n > 0) {
            for(int i = 1; i < s.length(); i++) {
                if(s[i] == s[i - 1]) {
                    count++;
                    if(i == s.length() - 1) {
                        str += to_string(count);
                        str.push_back(s[i - 1]);
                    }
                } else {
                    str += to_string(count);
                    str.push_back(s[i - 1]);
                    count = 1;

                    if(i == s.length() - 1) {
                        check = true;
                    }
                }
            }

            n--;
            if(n > 0) {
                s = str;
                str = "";
                count = 1;
            }

            if(check) {
                str += "1";
                str.push_back(s.back());
                check = false;
            }
        }

        return str;
    }
};
