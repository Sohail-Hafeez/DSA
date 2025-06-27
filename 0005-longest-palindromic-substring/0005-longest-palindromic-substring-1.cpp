class Solution {
public:
    bool checkPalidrome(string s, int j) {
        for (int i = 0; i < s.length(); i++) {
            if (i >= j) break;
            if (s[i] != s[j]) return false;
            j--;
        }
        return true;
    }

    string longestPalindrome(string s) {
        int max = 0;
        string a = "";
        a = a + s[0];
        string longest = "";
        bool bug = false;
        bool isPalindrome = false;

        if (s.length() == 1) {
            return s;
        } else if (s.length() == 2) {
            if (s[1] == s[0]) {
                return s;
            } else {
                return a;
            }
        }

        for (int i = 0; i < s.length(); i++) {
            for (int j = s.length() - 1; j > i; j--) {
                if (s[i] == s[j]) {
                    string str = s.substr(i, j - i + 1);
                    isPalindrome = checkPalidrome(str, str.length() - 1);
                    if (isPalindrome && str.length() > max) {
                        longest = str;
                        max = str.length();
                        bug = true;
                        if ((max * 100) / (s.length()) > 90) {
                            return str;
                        }
                    }
                }
            }
        }

        if (!bug) {
            return a;
        }
        return longest;
    }
};