class Solution {
public:
    bool isUgly(int n) {
        if (n<=0)
        {
            return false;
        }
        //int a[3]={2,3,5} ;
        for (int b:{2,3,5})
        {
            while (n%b==0)
            {
                n/=b;
            }
        }
        return n==1;

    }
};