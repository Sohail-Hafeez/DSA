class Solution {
public:
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        
        int i = nums.size()-k;
        vector<int> v;
        vector<int> result;
        vector<int> a = nums;
        sort(nums.begin(), nums.end());
        int j=0;
        if(k == nums.size())
        {
            return a;
        }
        while(k>0)
        {
                v.push_back(nums[i]);
           
            i++;
            k--;
        }
        for(int i=0; i<v.size(); i++)
        {
            for(int j=0; j<a.size(); j++)
            {
                if(a[j]==v[i])
                {
                    v[i]=INT_MIN;
                    result.push_back(a[j]);
                    break;
                }
            }
        }
        return result;
    }
};