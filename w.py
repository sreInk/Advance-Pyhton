number = [1,2,3,4]
n2 = [5,6,7,8]
result = map(lambda x,y:x+y,number,n2)
print(list(result))

num = [1,2,3,4,5]
def sq(n):
    return n*n
sqaure =list(map(sq,num))
print(sqaure)