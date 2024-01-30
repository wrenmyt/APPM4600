import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 11) 
y = np.arange(0, 11, 1)

x.size 
y.size 

x[1:4]

print('The first three entries of x are', x[:3])


w = 10**(-np.linspace(1,10,10))
x = np.arange(1, w.size+1, 1)
s = 3*w

plt.semilogy(x,w)
plt.plot(x,s)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()



