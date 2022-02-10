class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
         
   vector<int>numbsnew;

   int add;
   int a,b;
        

  for(int i = 0; i < nums.size(); i++){
            for(int j = i+1; j < nums.size();j++){
        add = nums[i] + nums[j];
        if ( add == target){
         a = i;
         b = j;
        numbsnew.push_back(a);
        numbsnew.push_back(b);
        }

            }
    }

    return numbsnew;
        
    }
};