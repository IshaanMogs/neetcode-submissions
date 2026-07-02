class Solution {
public:
    bool isPalindrome(string s) {
        int right = s.length()-1;
        int left = 0;
        while(left<right){
            if(!isalnum(s[left])){
                left++;
                continue;
            }
            if(!isalnum(s[right])){
                right--;
                continue;
            }
            if(tolower(s[left])==tolower(s[right])){
                left++;
                right--;
            }
            else{
                return false;
            }
        }
        return true;
    }
};