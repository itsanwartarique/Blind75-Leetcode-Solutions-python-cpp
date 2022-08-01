class Solution {
public:
    //Method 1
    int missingNumber(vector<int>& nums) {
        int result = nums.size(), i=0;
        for(int x: nums){
            result ^=x;
            result ^= i;
            i++;
        }
        return result;
    }
    
    // //Method 2
    // int missingNumber(vector<int>& nums) {
    //     int n = nums.size();
    //     int sum =0;
    //     for(int x: nums)sum+=x;
    //     return n*(n+1)/2 - sum;
    // }      
};