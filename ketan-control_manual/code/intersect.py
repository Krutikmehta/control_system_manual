#closed loop magnitude response
import control
from scipy import signal
import numpy as np 
import matplotlib.pyplot as plt 

#if using termux
import subprocess
import shlex
#end if

def M_circle(m):
  theta = np.linspace(0, 2*np.pi, 100)
  x0 = np.around(m**2/(1-m**2),decimals=2)
  y0 = np.around(0,decimals=2)
  r = abs(m/(1-m**2))
  x = x0 + r*np.cos(theta)
  y = y0 + r*np.sin(theta)
  return np.around(x,decimals=2),np.around(y,decimals=2)


#Creating a transfer function G = num/den
nume = 1000
deno = [1,18,119,342,360]
G = control.tf(nume,deno) 
niq = np.around(control.nyquist(G,Plot=0),decimals=2)

#finding the point of intersection
mag=np.empty(0)
freq=np.empty(0)
m=np.arange(0,8,0.02)
for num in m:
  if num != 1:
    for i in range (len(niq[0])):
      for j in range (len(M_circle(num)[0])):
        if niq[0][i] == M_circle(num)[0][j] and niq[1][i] == M_circle(num)[1][j]:
          mag=np.append(mag,num)
          freq=np.append(freq,niq[2][i])

print(mag)
print(len(mag))
print(freq)
print(len(freq))

sys = signal.TransferFunction(1000, [1,18,119,342,1360])
w, mag1, phase = sys.bode()
plt.subplot(2,1,1)
plt.semilogx(w, mag1,label='actual') 
plt.semilogx(freq,np.log(mag+10**(-50)), label='obtained from python code')
plt.legend()
plt.xlim([0,100])
plt.ylim(-90,15)
plt.title('magnitude vs freq')
plt.xlabel('freq')
plt.ylabel('M')

plt.subplot(2,1,2)
plt.semilogx(w, phase,label ='actual')
plt.legend()
plt.title("phase vs freq")
plt.savefig("plot.eps")
plt.show()

#if using termux
#plt.savefig('mag.eps')
#subprocess.run(shlex.split("termux-open mag.pdf"))
#plt.show()