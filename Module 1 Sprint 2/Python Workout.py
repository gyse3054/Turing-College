
#vovels = str('a' ,'e')
#print(vovels)
a = str('gytis')
print(a)
print(a[0])

def pig_latin():
    word = str(input('Write english word:')).lower()
    vovels = ['a', 'e', 'i', 'o', 'u']
    if word[0] in vovels:
        new_word = word + 'way'
    else:
        new_word = word[1:] + word[0] + 'ay'
    print(new_word)
    


pig_latin()