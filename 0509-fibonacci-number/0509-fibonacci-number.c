

int fib(int n)
{
    int a=0;
    int b=1;
    int temp;
    if(n==0)
    {return 0;}
    for (int i=1;i<n;i++)
    {
        temp=a;
        a=b;
        b=temp+a;

    }
    return b;
}