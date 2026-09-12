int countDigits(int num) {
    int n1=num;
    int n=0;
    while (num>0)
    {
        if (n1%(num%10)==0)
        {
            n++;
        }
        num=num/10;
    }
    return n;
}