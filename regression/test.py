import numpy as np
import matplotlib.pyplot as plt
x= np.array([1,2,3,4]).reshape(-1,1)
y= np.array([1,3,5,7])
plt.plot(x)
plt.show()
print(x)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(x,y)

result= model.predict([[5]])
print(result)
