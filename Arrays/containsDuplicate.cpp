class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        int len = nums.size();
        map<int,int>m;
        for(int i = 0; i<len; i++){
            if(m.find(nums[i])==m.end()){
                m[nums[i]] = 0;
            }
            else{
                return true;
            };
        }
        return false;
    }
};