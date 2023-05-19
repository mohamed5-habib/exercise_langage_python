def parfait(n):
    sum1 = 0
    test=True
    for i in range(1, n):
        if(n%i==0):
            sum1+=i
    if (sum1!=n):
        test=False
    return test

def premier(x):
    test=True
    for i in range(2, x//2):
        if (x%i==0):
            test=False
    return test

def premier_tab(x):
    tab=[]
    for i in range(2, x+1):
        if(premier(i)):
            tab.append(i)
    return tab

def supp(x, y, tab):
    for i in range(tab):
