
# print("Hello world")

# eqn = input("Enter your equation: ")
# eqn = eval(input("Enter your equation: "))
# print(eqn)
'''
1. Take input of the function
2. choose the a and b
3. write the value of x
'''

eqn = input("Enter your equation: ")
def f(x,eqn):
    x = x
    return eval(eqn)

def a(eqn):
    for i in range(-10,10):
        if f(i,eqn) < 0:
            return i
    return None
def b(eqn):
    for i in range(-10,10):
        if f(i,eqn) > 0:
            return i
    return None

def bisection(a,b,eqn):
    run = True
    cnt = 0
    while run:
        x = (a+b)/2
        if f(x,eqn) > 0:
            b = x
        else:
            a = x
        x1 = x
        cnt +=1
        # print(x)
        if cnt == 1000:
            run = False
            
    print(round(x,5))
    return x
    
a = a(eqn)
b = b(eqn)
ans = bisection(a,b,eqn)
print(f"Your root of the equation {eqn} using bisection method is: {ans}")
'''
* You can specify the iteration number in the method
'''