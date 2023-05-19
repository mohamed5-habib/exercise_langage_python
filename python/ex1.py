import string
alph_string = string.ascii_lowercase
alph_list = list(alph_string)
alph_list.append(" ")

def cryptage(ch):
    ch2=""
    for i in list(ch):
        if (i in alph_list):
            if (i==" "):
                ch2+=" "
            else:
                ch2+=chr(ord(i)+1)
        else:
            ch2+=i
    return ch2

ch = input("Donner une chaine des carateres: ")

print(cryptage(ch))
