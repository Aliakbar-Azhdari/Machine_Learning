# 1 => 1
# 2 => 3
# 3 => 5
# 4 => 7
# 5 => ?

# y = 2 * x -1

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([1 , 2 , 3 , 4]).reshape(-1 , 1)
y = np.array([1 , 3 , 5 , 7])

model = LinearRegression()
model.fit(x , y)

# # y = m * c + 1
# # m = 2 , c = -1

c = model.intercept_
m = model.coef_[0]
print(m , c , sep= " * ")

plt.plot(x , y , "*")
plt.plot(x , model.predict(x))
plt.show()
v = model.predict([[20]])
print(v)