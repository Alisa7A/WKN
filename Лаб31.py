x=int(input('4-digit:'))
c1=x%100
c1=c1//10
c2=x//100
c2=c2%10
S=c1+c2
D=c1*c2
print("сума двох середніх чисел :",S)
print("добуток двох середніх чисел",D)