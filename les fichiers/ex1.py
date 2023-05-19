f1=open('file.txt',"r") 
l=f1.readlines()
s=1
for i in l:
    print(str(s)+ i)
    s=s+1
print(l)
f1.close


