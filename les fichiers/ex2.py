f1=open('note.txt',"r") 
l=f1.readlines()
l1=[]
for i in l:
    l1.append(float(i))
print(l1)
f1.close
f2=open('note.txt',"w") 
for i in l1:
    if (i<10):
        f2.write(str(i)+"recalé")
    else:
        f2.write(str(i)+"admis")
f2.close