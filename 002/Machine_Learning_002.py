# 1 => 5
# 2 => 10
# 3 => 15
# 4 => 20
# 5 => ?

# y = 5 * x

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



x = np.array([1 , 2 , 3 , 4]).reshape(-1 , 1)
y = np.array([5 , 10 , 15 , 20])

model = LinearRegression()
model.fit(x , y)

m = model.coef_[0]
c = model.intercept_
print(m , c , sep=" * ")

plt.plot(x , y , " * ")
plt.plot(x , model.predict(x))
plt.show()

v = model.predict([[20]])
print(v)  # v => 100