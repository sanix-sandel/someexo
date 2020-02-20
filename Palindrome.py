
#first possibility

def palindrome(texte):
    texte1=texte[::-1]
    if texte==texte1:
        return (print("Yes, it's a palindrome"))
    else:
        return print("No, it's not a palindrome")


#Second

def checker(texte):
    n=len(texte)
    m=n-1
    i=0
    check=True
    while i<n and m>-1:
        if texte[i]!=texte[m]:
            ckeck=False
            break

        i+=1
        m-=1
    return check

def Palindrome(texte):
    if checker(texte):
        return print('Yeah, a palindrome')
    else:
        return print('No, not a palindrome')


if __name__=='__main__':
    palindrome('civic')
    Palindrome('civic')
