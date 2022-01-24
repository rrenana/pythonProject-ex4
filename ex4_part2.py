#Neville Method
#Noa Asulin , Michal Tenenboim, Renana Zinner


def Neville_Algorithm(xm, ym, xn, yn, x):
    p = ((x - xm)*yn - (x-xn)*ym) / (xn-xm)
    return p

def main ():
    # Table points
    x0 = 1
    y0 = 0
    x1 = 1.2
    y1 = 0.112463
    x2 = 1.3
    y2 = 0.167996
    x3 = 1.4
    y3 = 0.222709

    # Finding the value of the function at a given point
    x = 1.28

    #calculation
    p01 = Neville_Algorithm(x0, y0, x1, y1, x)
    p12 = Neville_Algorithm(x1, y1, x2, y2, x)
    p23 = Neville_Algorithm(x2, y2, x3, y3, x)
    p02 = Neville_Algorithm(x0, p01, x2, p12, x)
    p13 = Neville_Algorithm(x0, p12, x2, p23, x)
    p03 = Neville_Algorithm(x0, p02, x2, p13, x)
    print("The result is:")
    print(p03)

main()
