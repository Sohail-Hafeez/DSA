class Solution {
public:
    bool isPalindrome(string s) {
        string str = "";
        for(int i=0; i<s.size(); i++)
        {
            if(s[i]>=97 && s[i]<=122 || s[i]>=48 && s[i]<=57)
            {
                str.push_back(s[i]);
            }
            else if(s[i]>=65 && s[i]<=90)
            {
                char a = s[i] + 32;
                str.push_back(a);
            }
        }
        int j = str.length()-1;
        for(int i = 0; i<str.length(); i++)
        {
            if(i<j)
            {
                if(str[i]!=str[j])
                {
                    return false;
                }
            }
            else
            {
                break;
            }
            j--;
        }
        return true;
    }
};