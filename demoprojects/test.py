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

# list = [1]*5 + [2]*3 +[3]*2
# print(list)

def testString():
    str = "taaaaeraataaaatdfaaawaawtaaaaaaasa"
    print("length of the string: ",len(str))
    temp = ''
    prev = ''
    flag = 1
    list = []
    count = 0
    for ch in str:
        count+=1
        if (ch == 'a'):
            flag = 1
            temp = temp + 'a'
        elif (ch != 'a' and prev == 'a' and flag == 1):
            list.append(temp)
            flag = 0
            temp = ''
        else:
            flag = 0

        if (count == len(str)-1 and ch == 'a' and prev != 'a'):
            list.append(ch)
            print("test---------")    
        prev = ch       
    print("final list is: ",list)   

# testString()      

