#square
def square(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print()
#right angle pyramid       
def righttri(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print()
#inverted right pyramid
def inverted(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end=" ")
        print()
 #number right angle triangle       
def numrighttri(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
def numrighttri2(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print()


#inverted number right angle triangle
def invnum(n):
    for i in range(1,n+1):
        for j in range(1,(n+1)-i+1):
            print(j,end=" ")
        print()


