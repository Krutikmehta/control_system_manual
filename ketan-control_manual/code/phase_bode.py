#closed loop magnitude response
from scipy import signal
import numpy as np 
import matplotlib.pyplot as plt 

#if using termux
import subprocess
import shlex
#end if

sys = signal.TransferFunction([1000], [1,18,119,342,1360])
w, mag, phase = sys.bode()
plt.figure()
plt.semilogx(w, mag) 
plt.figure()
plt.semilogx(w, phase)  # Bode phase plot
plt.show()