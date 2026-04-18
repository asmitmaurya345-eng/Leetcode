def myAtoi(s):
    a=s.strip()
    c=0
    if a=="":
        return 0
        elif a[0]=="-":
            c=1
            a=a[1:]
        elif a[0]=="+":
            a=a[1:]
    b=0
    for x in a:
        if x.isdigit():
            b=b*10+int(x)
        else:
            break
    if c==1:
        b*=-1
    if b<-2147483648:
        b=-2147483648
    elif b>2147483647:
        b=2147483647
    return b
