import pandas as pd
import matplotlib.pyplot as pt

data = pd.read_csv('placement.csv')
def linear_gradient(m_old, c_old, data, learning_rate):
    temp1 = 0
    temp2 = 0
    for i in range(len(data)):
        temp1 = temp1 + (data[['y']].iloc[i] -(m_old*data[['x']].iloc[i]+c_old))*(-data[['x']].iloc[i])
        temp2 = temp2 + (data[['y']].iloc[i]-(m_old*data[['x']].iloc[i]+c_old))*(-1)
    m_new = m_old - learning_rate*(2/len(data))*temp1
    c_new = c_old - learning_rate*(2/len(data))*temp2
    return [m_new, c_new]
m = 0
c = 0
learning_rate = 0.0001
for i in range(10):
    print(i)
    [m, c] = linear_gradient(m, c, data, learning_rate)

x_list = []
y_list = []
for i in range(0,101):
    x_list.append(i)
    y_list.append(1*i+0)
pt.scatter(data[['x']], data[['y']], color="red")
pt.plot(x_list, y_list, color="black")
pt.show()