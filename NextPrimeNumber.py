
"""
Next Prime Number - Have the program find prime numbers until
the user chooses to stop asking for the next one.
"""

from itertools import*

def isprime(x):
    liste=[y for y in range(2, x) if not x%y]
    if len(liste)==0:
        return True
    else:
        return  False

liste=(x for x in count(start=1, step=1) if isprime(x))

"""
def findprime():
    
    for x in count(start=1, step=1):
        if isprime(x):
            yield x
  
  """


if __name__=='__main__':
    #a = findprime()
    while True:
        print('Next prime number ?')
        answer=input()
        if answer=='':
            print(next(liste))
        else:
            break
