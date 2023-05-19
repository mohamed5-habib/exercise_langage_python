liste=[]
liste1=[]
n = int(input("Donner n: "))

def test(x):
    for i in range(2, int(x/2)):
        if (x%i==0):
            return False
        else:
            return True

for i in range(1, n):
    if (test(i)==True):
        liste.append(i)

print(liste)