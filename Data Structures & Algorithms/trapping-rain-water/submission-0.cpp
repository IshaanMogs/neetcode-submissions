class Solution {
public:
    int trap(vector<int>& height) {
        int max_right = 0;
        int max_left = 0;
        int right = height.size()-1;
        int left = 0;
        int trapped = 0;
        while(left<right){
            if(height[left]<height[right]){
                int curr_left = height[left];
                if(height[left]>max_left){
                    max_left = height[left];
                }
                trapped += max_left-curr_left;
                left++;
            }
            else{
                int curr_right = height[right];
                if(height[right]>max_right){
                    max_right = height[right];
                }
                trapped += max_right - curr_right;
                right--;
            }
        }
        return trapped;
    }
};