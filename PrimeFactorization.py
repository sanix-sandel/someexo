"""
Prime Factorization - Have the user enter a number and find
 all Prime Factors (if there are any) and display them.

"""



def primenumber(x):
    liste=[y for y in range(2, x) if not x%y]
    if len(liste)==0:
        return True
    else:
        return False



if __name__=='__main__':
    number = int(input())
    factors = [x for x in range(2, number) if not number % x]
    primeliste = [y for y in factors if primenumber(y) == True]
    print(primeliste)