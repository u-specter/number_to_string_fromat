x=int(input())
c=1
lst = []

x1=x//1000
if x1 == 9:
    lst.append('toqqizming')
    # print()
elif x1 == 8:
    lst.append('sakkizming')
    # print()
elif x1 == 7:
    lst.append(' yettiming')
    # print()
elif x1 == 6:
    lst.append(' oltiming')
    # print()
elif x1 == 5:
    lst.append(' beshming')
    # print()
elif x1 == 4:
    lst.append(' tortming')
    # print()
elif x1 == 3:
    lst.append(' uchming')
    # print()
elif x1 == 2:
    lst.append(' ikkiming')
    # print()
elif x1 == 1:
    lst.append(' birming')
    # print()
else:
    lst.append('')
    # print()
    
x1=x%1000//100

if x1 == 9:
    lst.append('toqqizyuz')
    # print()
elif x1 == 8:
    lst.append('sakkizyuz')
    # print()
elif x1 == 7:
    lst.append(' yettiyuz')
    # print()
elif x1 == 6:
    lst.append(' oltiyuz')
    # print()
elif x1 == 5:
    lst.append(' beshyuz')
    # print()
elif x1 == 4:
    lst.append(' tortyuz')
    # print()
elif x1 == 3:
    lst.append(' uchyuz')
    # print()
elif x1 == 2:
    lst.append(' ikkiyuz')
    # print()
elif x1 == 1:
    lst.append(' biryuz')
    # print()
else:
    lst.append('')
    # print()
x1=x%100//10

if x1 == 9:
    lst.append(' toqson')
    # print()
elif x1 == 8:
    lst.append(' sakson')
    # print()
elif x1 == 7:
    lst.append(' yetmish')
    # print()
elif x1 == 6:
    lst.append(' oltmish')
    # print()
elif x1 == 5:
    lst.append(' ellik')
    # print()
elif x1 == 4:
    lst.append(' qiriq')
    # print()
elif x1 == 3:
    lst.append(' o\'ttiz')
    # print()
elif x1 == 2:
    lst.append(' yigirma')
    # print()
elif x1 == 1:
    
   
    x1=x%10

    c=0

    if x1 == 9:
        lst.append(' o\'n toqqiz')
        # print()
    elif x1 == 8:
        lst.append(' o\'n sakiz')
        # print()
    elif x1 == 7:
        lst.append(' o\'n yetti')
        # print()
    elif x1 == 6:
        lst.append(' o\'n olti')
        # print()
    elif x1 == 5:
        lst.append(' o\'n besh')
        # print()
    elif x1 == 4:
        lst.append(' o\'n to\'rt')
        # print()
    elif x1 == 3:
        lst.append(' o\'n uch')
        # print()
    elif x1 == 2:
        lst.append(' o\'n ikki')
        # print()
    elif x1 == 1:
        lst.append(' o\'n bir')
        # print()
    else:
        lst.append('o\'n')
        # print()

if c==1:
    x1=x%10
    if x1 == 9:
        lst.append(' toqqiz')
        # print()
    elif x1 == 8:
        lst.append(' sakiz')
        # print()
    elif x1 == 7:
        lst.append(' семь')
        # print()
    elif x1 == 6:
        lst.append(' olti')
        # print()
    elif x1 == 5:
        lst.append(' besh')
        # print()
    elif x1 == 4:
        lst.append(' to\'rt')
        # print()
    elif x1 == 3:
        lst.append(' uch')
        # print()
    elif x1 == 2:
        lst.append(' ikki')
        # print()
    elif x1 == 1:
        lst.append(' bir')
        # print()
    elif x1 == 0:
        lst.append('nol')
        # print()
son = ''.join(lst)     
print(son)        