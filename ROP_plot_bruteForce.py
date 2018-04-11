import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
from matplotlib.mlab import  bivariate_normal
def get_test_data(delta=0.05):

    
    x = y = np.arange(-3.0, 3.0, delta)
    X, Y = np.meshgrid(x, y)

    Z1 = bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
    Z2 = bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
    Z = Z2 - Z1

    X = X * 10
    Y = Y * 10
    Z = Z * 500
    return X, Y, Z



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x, y, z = get_test_data(0.05)
ax.plot_surface(x,y,z, rstride=3, cstride=10,cmap=cm.coolwarm)
ax.set_xlabel('WOB Label')
ax.set_ylabel('RPM Label')
ax.set_zlabel('ROP Label')

n,m = 120,120
q,p = 0,0
best_ROP = 0
best_WOB = 0
best_RPM = 0
number_itr = 0
for i in range(q,n):
    for j in range(p,m-1):
        number_itr +=1          
        if z[i,j] > best_ROP:
            plt.plot([x[i,j]],[y[i,j]],[z[i,j]], markerfacecolor='k',
                markeredgecolor='k', marker='o', markersize=2, alpha=0.6)
            best_ROP =  z[i,j]
            best_RPM = x[i,j]
            best_WOB = y[i,j]
      
print("Best ROP = " + str(best_ROP) + " with RPM = " + str(best_RPM) + " and WOB = " + str(best_WOB))      
plt.show()               
print("Number of itterations: " + str(number_itr))