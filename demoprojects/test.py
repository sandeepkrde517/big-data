print("test demo")

## print() menthod demo
def printDemo():
    a=10
    b=20
    c=30
#f= open('abc.txt', 'w')
 #   print(a,b,c, sep='..', end='#', file=open('abc.txt', 'w'))

#############################################################

## input() demo
def inputDemo():
    list = [int(n) for n in input("enter three nos ").split(" ")]
    first, middle, last = list
    print(first, middle, last, sep='$$')

#printDemo()
#

#####################

list = [1]*5 + [2]*3 +[3]*2
print(list)