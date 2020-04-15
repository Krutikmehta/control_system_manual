import matplotlib.pyplot as plt
import math
import numpy as np

x=np.linspace(0,3,1000)
y=np.arctan(2*x/np.sqrt(np.sqrt(1+4*x**4)-2*x**2))*(360/2*np.pi)
plt.xlabel('damping ratio')

 

# Give y axis label for the semilog plot

plt.ylabel('phase margin')

plt.plot(x,y)
plt.savefig('realtion')
plt.show()