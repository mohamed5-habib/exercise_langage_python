def recherche(tab, ch):
    if (ch in tab):
        return True
    else:
        return False

tab = [i for i in input("Donner les element de tableau: ").split(' ')]
ch = input("Donner les l'element a recherche: ")

print(tab)

if (recherche(tab, ch)):
    print("Existe!")
else:
    print("N'exsite pas!")
