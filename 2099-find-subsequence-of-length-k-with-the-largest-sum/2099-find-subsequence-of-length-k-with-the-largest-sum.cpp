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
        for(int i=0; i<a.size(); i++)
        {
            for(int j=0; j<v.size(); j++)
            {
                if(a[i]==v[j])
                {
                    v[j]=INT_MIN;
                    result.push_back(a[i]);
                    break;
                }
            }
        }
        return result;
    }
};