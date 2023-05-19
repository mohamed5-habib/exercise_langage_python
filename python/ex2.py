def fact(x):
    if (x==0):
        return 1
    else:
        reste=1
        for i in range(1, x+1):
            reste*=i
        return reste

def unFact(x):
    if (x==1):
        return 0
    else:
        i=1
        reste=0
        aux=x
        while ((aux!=1) and (reste==0)):
            aux=aux//i
            reste=aux%i
            i+=1
        return i+1

while(True):
    print(fact(int(input("Donner un entier: "))))
    print(unFact(int(input("Donner un factorielle: "))))
