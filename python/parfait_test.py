n = int(input("Enter any number: "))
sum1 = 0
test=True
for i in range(1, n):
    if(n%i==0):
        sum1+=i
if (sum1!=n):
    test=False
