fecha_manchas.pdf : grafica.py fecha_manchas.dat
	python3 grafica.py
fecha_manchas.dat : procesa.py monthrg.dat
	python3 procesa.py
