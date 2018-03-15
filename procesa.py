import numpy as np
Data=np.loadtxt('monthrg.dat')
Ano=Data[:,0]
Mes=Data[:,1]
Dias=Data[:,2]
Manchas=Data[:,3]
index= Dias>0
Manchas=Manchas[index]
tiempo=Ano[index] + (Mes[index]/12.0)
X=np.array([tiempo,Manchas])
X=np.transpose(X)
np.savetxt('fecha_mancha.dat',X)
