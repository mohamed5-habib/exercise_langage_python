liste = []
x = input("Donner un nombre: ")
for i in x:
    liste.append(int(i))

print(liste)

result=0
for i in liste:
    result+=(i*i*i)

print(result)

if (result==int(x)):
    print("Armstrong")
else:
    print("N'est pas Armstrong")