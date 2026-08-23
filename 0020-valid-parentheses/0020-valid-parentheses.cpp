class Solution {
public:
    bool isValid(string s) {
        int len = s.length();
    char a[len+1];
    int index=0;
    for (char x:s)
    {
        if (x=='['||x=='{'||x=='(')
        {
            a[index]=x;
            index++;
        }
        else if (index>0 && x==']' && a[index-1]=='[')
        {
            a[index-1]='0';
            index--;
        }
        else if (index>0 && x=='}' && a[index-1]=='{')
        {
            a[index-1]='0';
            index--;
        }
        else if (index>0 && x==')' && a[index-1]=='(')
        {
            a[index-1]='0';
            index--;
        }
        else{return false;}
    }
    if (index==0)
    {return true;}
    return false;
        
    }
};