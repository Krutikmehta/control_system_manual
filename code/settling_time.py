import matplotlib.pyplot as plt
import numpy as np


x=np.linspace(0,25,1000)
y1=2*(np.exp(-x/6))*(np.sin(((11)**0.5)*x/6))/ ((11)**0.5)
y2=2*(np.exp(-x/2))*(np.sin((3)**0.5)*x/2)/((3)**0.5)
u1=1 -((np.exp(-x/6))*(np.cos(((11)**0.5)*x/6)))-((np.exp(-x/6))*(np.sin(((11)**0.5)*x/6))/((11)**0.5))
u2=1 -((np.exp(-x/2))*(np.cos(((3)**0.5)*x/6)))-((np.exp(-x/2))*(np.sin(((3)**0.5)*x/6))/((3)**0.5))

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
