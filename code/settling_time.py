import matplotlib.pyplot as plt
import numpy as np


x=np.linspace(0,10,1000)
y1=1-np.exp(-x/3)
y2=1-np.exp(-x)
u1=x+3*np.exp(-x/3)-3
u2=x+np.exp(-x)-1

plt.subplot(2,1,1)
plt.xlabel('t')
plt.ylabel('output')
plt.title('impulse response')
plt.plot(x,y1, label = 'Without Compensator')
plt.plot(x,y2, label = 'With Compensator')
plt.grid()
plt.legend()

plt.subplot(2,1,2)
plt.xlabel('t')
plt.ylabel('output')
plt.title('unit step response')
plt.plot(x,u1, label = 'Without Compensator')
plt.plot(x,u2, label = 'With Compensator')
plt.grid()
plt.legend()

plt.savefig('settling_time.pdf')

plt.show()