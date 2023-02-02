'''
to do:
1. summation, mean etc math operations can be done simply using numpy functions. see greg hogg's video to know how to do that
2. debug this code and get it up and workin'
3. know about eye doctor's formula discussed in greg hogg's video
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

data = pd.read_csv('placement.csv')
x = data['x']
y = data['y']
# pt.scatter(x, y, color="red")
# pt.show()
def gradient_descent(m_old, c_old, learning_rate):
    m_gradient = 0.0
    c_gradient = 0.0
    n = len(x)
    for i in range(362):
        m_gradient = np.float64(m_gradient) + (y[i] -(m_old*x[i]+c_old))*(-x[i])*(1/n)
        c_gradient = np.float64(c_gradient) + (y[i]-(m_old*x[i]+c_old))*(-1)*(1/n)
        print("i: ", i)
        print("m_gradient: ", m_gradient)
        print("c_gradient: ", c_gradient)
    # print(-843.5620984605345-(y[212]*x[212])/n)
    # print(-13.585226418299998-(y[212])/n)
    # print("vvvvvvvvvvvv")
    # print(-857.8500702605345, type(-857.8500702605345))
    # print((y[213]*x[213])/n, type((y[213]*x[213])/n))
    # print(-857.8500702605345-(y[213]*x[213])/n, type(-857.8500702605345-(y[213]*x[213])/n))
    # print(m_gradient)
    # print(c_gradient)
    # m_new = m_old - learning_rate*m_gradient
    # c_new = c_old - learning_rate*c_gradient
    # return m_new, c_new
    return 6, 4


m = 0
c = 0
learning_rate = 0.0001
mn, cn = gradient_descent(m, c, learning_rate)

# x_list = []
# y_list = []
# for i in range(0,101):
#     x_list.append(i)
#     y_list.append(1*i+0)
# pt.scatter(data[['x']], data[['y']], color="red")
# pt.plot(x_list, y_list, color="black")
# pt.show()