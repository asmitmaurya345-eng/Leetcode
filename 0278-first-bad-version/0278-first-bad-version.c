// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

int firstBadVersion(long int n) 
{
    long int l=1;
    while (l<n)
    {
        long int m=(l+n)/2;
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