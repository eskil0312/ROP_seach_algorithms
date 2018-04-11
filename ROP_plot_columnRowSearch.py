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





number_itr = 0

arrayMaxROP_RPM = 0
arrayMaxROP_WOB = 0
RPM_i = 0
WOB_j = 0
WOB_j = int(WOB_j)

itr_since_best_ROP = 0
new_best_ROP = False
while True:
    i = 0
    new_best_ROP = False
    itr_since_best_ROP = 0
    while i < n:
        number_itr +=1
        itr_since_best_ROP += 1
        #This possible implmentation does not garantee as good result, but number of itr reduce drastically
        if itr_since_best_ROP >5 and new_best_ROP == True:
            pass
            #break
        if z[WOB_j,i] > arrayMaxROP_RPM:
            new_best_ROP = True
            itr_since_best_ROP = 0
            arrayMaxROP_RPM = z[WOB_j,i]
            RPM_i = i
        i+=1
        
        plt.plot([x[WOB_j,RPM_i]],[y[WOB_j,RPM_i]],[z[WOB_j,RPM_i]], markerfacecolor='r', markeredgecolor='k', marker='o', markersize=5, alpha=0.6)
    
    plt.plot([x[WOB_j,RPM_i]],[y[WOB_j,RPM_i]],[z[WOB_j,RPM_i]], markerfacecolor='k', markeredgecolor='k', marker='o', markersize=5, alpha=0.6)
    
    
    j = 0
    new_best_ROP = False
    itr_since_best_ROP = 0
    while j < m:
        number_itr +=1
        itr_since_best_ROP += 1
        #This possible implmentation does not garantee as good result, but number of itr reduce drastically
        if itr_since_best_ROP >5 and new_best_ROP == True:
            pass
            #break
        if z[j,RPM_i] > arrayMaxROP_WOB:
            new_best_ROP = True
            itr_since_best_ROP = 0
            arrayMaxROP_WOB = z[j,RPM_i]
            WOB_j = j
        j +=1
        plt.plot([x[WOB_j,RPM_i]],[y[WOB_j,RPM_i]],[z[WOB_j,RPM_i]], markerfacecolor='r', markeredgecolor='k', marker='o', markersize=5, alpha=0.6)
            
    plt.plot([x[WOB_j,RPM_i]],[y[WOB_j,RPM_i]],[z[WOB_j,RPM_i]], markerfacecolor='k', markeredgecolor='k', marker='o', markersize=5, alpha=0.6)
    
    
    if arrayMaxROP_WOB == arrayMaxROP_RPM:
        print("Best ROP found at " + str(x[WOB_j,RPM_i]) +(", ")+ str(y[WOB_j,RPM_i]) + " with ROP: "+ str(z[WOB_j,RPM_i]))
        break

plt.show()
print("Number of itterations: " + str(number_itr))
        