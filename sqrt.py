n=complex(input('number?'))
tolerance=1e-8

low=0

if n.imag!=0 or n.real<0:
    phase=n.imag/n.real
    n=abs(n)
 
low=0
if abs(n)>=1:
    high=abs(n)
else:
    high=1

mid=(low+high)/2
while abs(n-mid**2)>=tolerance:
    mid=(low+high)/2
    if mid**2<n:
        low=mid
    else: 
        high=mid
    print(low,high)

print(high) 
