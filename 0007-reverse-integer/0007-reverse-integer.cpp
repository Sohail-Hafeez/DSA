class Solution {
public:
    int reverse(int x) {
        int a = 1;
        bool check = true;
        int result = 0;
        string s = to_string(x);
        
        for(int i = s.length()-1; i>=0; i--)
        {
            if(s[0]=='-')
            {
                a = -1;
            }
            if(s[i]=='0' && check)
            {
                continue;
            }
            else if(s[i]!='0')
            {
                check = false;
                s = s.substr(0, i+1);
                std::reverse(s.begin(), s.end());
                break;
            }
        }
        long long b = stoll(s);
        if(b>pow(-2,31) && b <pow(2,31)-1)
        {
            result = b;
            return result*a; 
        }
        else
        {
            return 0;
        }

    }
};