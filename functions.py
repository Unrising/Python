# functions = a block of wich is executed only when it is called


def sum(a,b):
    
    return a + b


print(sum(1,3))


def hello():

    print("hello")

hello()


def calcul(a,b,c):

    if(c == '+'):
       return(a + b)
    elif(c == '/'):
        return(a / b)
    else:
        print("This is not going to work")
        print(c + " is not valable")

def hello(name):
    print("hello "+ name)


name = "Michael"

hello(name)

print(calcul(5,6,'+'))

print(calcul(4,2,'/'))

print(calcul(4,2,'*'))


def concatenate(first,last,birth):
    age = 2024 - birth
    return first +" "+ last + "and you are " + str(age)

print(concatenate("Michael","Picard",1999))