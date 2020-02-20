def findpig(texte):

    function = lambda x: x[1:]+x[0]+"ay" if x.isalpha()==True else x
    liste=texte.split()
    liste=list(map(function, liste))
    texte=" ".join(liste)
    return print(texte)

if __name__=='__main__':
    texte=input()
    findpig(texte)
