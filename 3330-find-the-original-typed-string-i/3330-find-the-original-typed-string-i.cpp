class Solution {
public:
    int possibleStringCount(string s) {
        bool check = true;
        int count = 0;
        bool ant = false;
        for(int i=1; i<s.length(); i++)
        {
            if(i>1)
                {
                    ant = false;
                }
            if(s[i]==s[i-1])
            {
                check =false;
                count++;
                
                if(s[i]==s[i+1] && i+1 <= s.length()-1)
                {
                    i++;
                    ant = true;
                    while(s[i]==s[i-1] && i <= s.length()-1)
                    {
                        i++;
                        continue;
                    }
                }
            }
        }
        if(check)
        {
            return 1;
        }
        if(ant && count ==1 && s.length()>2)
        {
            return s.length();
        }
        if(s.length()<=2)
        {
            return s.length();
        }
        return  s.length()-count;
    }
};