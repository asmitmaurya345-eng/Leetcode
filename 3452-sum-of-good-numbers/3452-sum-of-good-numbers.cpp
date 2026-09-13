class Solution {
public:
    int sumOfGoodNumbers(vector<int>& num, int k) {
        
        int n=0;
        int l=num.size();
        for (int x=0;x<l;x++)
        {
            if ((x-k < 0 || num[x] > num[x-k]) && (x+k >= l || num[x] > num[x+k]))
            {
                    n=n+num[x];
            }
        }
        return n;
    }
};