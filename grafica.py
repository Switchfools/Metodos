import matplotlib.pylab as plt
import numpy as np
Data=np.loadtxt('fecha_mancha.dat')
plt.plot(Data[:,0],Data[:,1],color='teal')
plt.xlabel("Tiempo(años)")
plt.ylabel("Numero Manchas Solares")
plt.title("Manchas Solares")
plt.savefig('fecha_mancha.pdf')
