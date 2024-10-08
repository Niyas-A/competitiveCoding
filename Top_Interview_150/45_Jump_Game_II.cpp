class Solution {
public:
    int jump(vector<int>& nums) {
        int left=0, right=0, jumps=0;
        while (right<size(nums)-1){
            int biggest_jump=0;
            for (int i=left;i<right+1;i++){
                biggest_jump=max(biggest_jump, i+nums[i]);
            } 
            left=right;
            right=biggest_jump;
            jumps+=1;
        }
        return jumps;
    }
};