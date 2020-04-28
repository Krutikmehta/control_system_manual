#closed loop magnitude response
import control
import numpy as np 
import matplotlib.pyplot as plt 

#if using termux
import subprocess
import shlex
#end if

def M_circle(m):
  theta = np.linspace(0, 2*np.pi, 100)
  x0 = m**2/(1-m**2)
  y0 = 0
  r = np.absolute(m/(1-m**2))
  x = x0 + r*np.cos(theta)
  y = y0 + r*np.sin(theta)
  return np.around(x,decimals=2),np.around(y,decimals=2)


#Creating a transfer function G = num/den
nume = 1000
deno = [1,18,119,342,360]
G = control.tf(nume,deno) 
w=np.logspace(-100,100,200)
niq = np.around(control.nyquist(G,Plot=0),decimals=2)

#finding the point of intersection
mag=np.empty(0)
freq=np.empty(0)
m=np.arange(0,3,0.05)
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


plt.semilogx(freq,np.log(mag+10**(-200)))
plt.xlim([2,100])
plt.ylim(-90,5)
plt.title('magnitude vs freq')
plt.xlabel('freq')
plt.ylabel('M')
plt.savefig("mag.eps")
plt.show()

#if using termux
#plt.savefig('mag.eps')
#subprocess.run(shlex.split("termux-open mag.pdf"))
#plt.show()