class Solution {
public:
    int findLucky(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int count = 1;
        int result = 0;
        for(int i = 1; i<arr.size(); i++)
        {
            if(arr[i]==arr[i-1])
            {
                count++;
                if(i==arr.size()-1)
                {
                    if(count == arr[i-1])
                {
                    result = arr[i-1];
                }
                }
            }
            else
            {
                if(count == arr[i-1])
                {
                    result = arr[i-1];
                }
                count = 1;
            }
            if(i == arr.size()-1 && result > 0 )
            {
                if(count == arr[i-1])
                {
                    result = arr[i-1];
                }
                count = 1;
                return result;
            }

        }
        
        return -1;
    }
};