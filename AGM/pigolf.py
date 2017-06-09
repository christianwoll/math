K=1003
def s(n):
    x,y=n,n>>1
    while y<x:x,y=y,(y+n//y)>>1
    return x
t,a,b,p=10**K//4,10**K,s(2*10**(2*K))//2,1
while 2*p<K:t,a,b,p=t-p*((a-b)//2)**2//10**K,(a+b)//2,s(a*b),2*p
print('3.'+str((a+b)**2//(4*t))[1:-3])
