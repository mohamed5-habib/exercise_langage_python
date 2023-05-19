f1=open('file.txt',"r") 
l=f1.readlines()
s=1
for i in l:
    print(str(s)+ i)
    s=s+1
print(l)
f1.close
f2=open("file.txt","w")
s=1
for i in l:
    f2.write(str(s)+i)
    s=s+1
f2.close
