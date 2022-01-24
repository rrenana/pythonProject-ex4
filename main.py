#Newton Rapson Method
#Noa Asulin , Michal Tenenboim, Renana Zinner
import sympy as sp
from sympy.utilities.lambdify import lambdify
x = sp.symbols('x')


def Newton_Rapson(func, func2, num, count):
    epsilon = 0.0001
    if func(num) == 0:
        return num, count
    else:
        valFunc = func(num)
        valDiff = func2(num)
        result = num - (valFunc / valDiff)
        if abs(result - num) < epsilon:
            return result, count
        else:
            count = count + 1
            return Newton_Rapson(func, func2, result, count)

def Parts (a, b):
    count = (b-a)/0.1
    return count

def check (a, b, func):
    if func(a) * func(b) < 0:
        return 0
    else:
        return 1

#The main function
def main():
    a = -2
    b = 2
    my_f = x ** 2 - 2
    my_f1 = sp.diff(my_f)
    my_f = lambdify(x, my_f)
    my_f1 = lambdify(x, my_f1)


    amount = int(Parts(a, b))
    for i in range(amount):
        new = a + 0.1
        if check(a, new, my_f) == 0:
            count = 0
            start_x = (a + new) / 2
            result, count1 = Newton_Rapson(my_f, my_f1, start_x, count)
            print("The root of the equation in the segment is:")
            print(result)
            print("Number of iterations:")
            print(count1)
            print(""
                  "")
            a = new
        else:
            a = new

main()