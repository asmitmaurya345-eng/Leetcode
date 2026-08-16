int search(int* nums, int numsSize, int target) {
    int l=0;
    int h=numsSize-1;
    while (l<=h)
    {
        int m=(l+h)/2;
        if (nums[m]==target)
        {
            return m;
        }
        else if (nums[m]>target)
        {
            h=m-1;
        }
        else if (nums[m]<target)
        {
            l=m+1;
        }
    }
    return -1;
}