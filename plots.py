import control
import numpy as np
import matplotlib.pyplot as plt


def M_circle(m):
  theta = np.linspace(0, 2*np.pi, 100)
  x0 = m**2/(1-m**2)
  y0 = 0
  r = np.absolute(m/(1-m**2))
  x = x0 + r*np.cos(theta)
  y = y0 + r*np.sin(theta)
  return x,y,r,x0,y0

def N_circle(n):
  theta = np.linspace(0, 2*np.pi, 100)
  x0 = -0.5
  y0 = 1/(2*n)
  r = np.sqrt((1/4) + (1/(4*n**2)))
  x = x0 + r*np.cos(theta)
  y = y0 + r*np.sin(theta)
  return x,y,r,x0,y0

m=np.arange(0,3,0.2)
for num in m: 
    if num != 1:
      p=M_circle(num)
      plt.plot(p[0],p[1] )
      plt.title('M circles')
      plt.xlabel('Re(s)')
      plt.ylabel('Im(s)')
      if (num >= 0.6 and num <= 1):
        plt.text(0.8*(p[3]+p[2]),0.8*(p[4]+p[2]),np.around(num,decimals=2))
      elif (num >=1.4  and num <= 1.6):  
        plt.text(0.8*(p[3]-p[2]),0.8*(p[4]-p[2]),np.around(num,decimals=2))
    
plt.xlim(-5,5)
plt.ylim(-2,2)
plt.savefig("M")
plt.show()


n=np.arange(-2,2,0.2)
for num in n:
  if num != 0:
    q=N_circle(num)
    plt.plot(q[0],q[1] )
    plt.title('N circles')
    plt.xlabel('Re(s)')
    plt.ylabel('Im(s)')
    if num == 0.2 :
        plt.text(1.25*(q[3]-q[2]),0.2*(q[4]+q[2]),np.around(num,decimals=2))
    elif num == 0.4 :
        plt.text(q[3]-q[2],0.2*(q[4]+q[2]),np.around(num,decimals=2))    
    elif num == -0.4:    
        plt.text(1.15*(q[3]-q[2]),0.65*(q[4]-q[2]),np.around(num,decimals=2))
    elif num == -0.6:    
        plt.text(0.6*(q[3]-q[2]),0.65*(q[4]-q[2]),np.around(num,decimals=2))
   
plt.xlim(-5,5)
plt.ylim(-2,2)
plt.savefig("N")
plt.show()


nume = 1000
deno = [1,18,119,342,360]

#Creating a transfer function G = num/den
G = control.tf(nume,deno) 
w=np.logspace(-100,100,10000)
control.nyquist(G,w)
plt.grid(True)
plt.title('Nyquist Diagram of G(s) = 5/(s+1)(s+2)(s+3)')
plt.xlabel('Re(s)')
plt.ylabel('Im(s)')
plt.savefig("niquest")
plt.show()




