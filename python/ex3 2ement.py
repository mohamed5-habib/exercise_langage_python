def recherche(tab, tab2):
    test=True
    for i in range(len(tab)):
        if(tab[i] not in tab2):
            test=False
            break
    return test

tab = [i for i in input("Donner les element de tableau: ").split(' ')]
tab2 = [i for i in input("Donner les element de tableau 2: ").split(' ')]

print(tab)
print(tab2)

if (recherche(tab, tab2)):
    print("Existe!")
else:
    print("N'exsite pas!")
