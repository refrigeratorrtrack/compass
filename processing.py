import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


# Загрузка данных
data = np.loadtxt("data/1.txt", delimiter=" ", dtype=np.float)
polarDegree = []

for i in range(len(data)):
    polarDegree.append((data[i][4] - data[i][5]) / (data[i][4] + data[i][5]))
    print(str(i + 1) + " " + str(polarDegree[i]))
