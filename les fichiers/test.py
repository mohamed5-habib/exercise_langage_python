f1=open('file.txt',"r") 
l=f1.readlines()
print(l)
l[2]="oops\n"
print(l)
f1.close
f2=open("file.txt","w")
for i in l:
    f2.write(i)
f2.close
