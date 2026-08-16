// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

int firstBadVersion(int n) 
{
    int l=1;
    while (l<n)
    {
        int m=l+(n-l)/2;
        if (isBadVersion(m))
        {
            n=m;
        }
        else
        {
            l=m+1;
        }
    }
    return l;
}