import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
from matplotlib.mlab import  bivariate_normal

def get_plot_data(delta=0.05):
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

x, y, z = get_plot_data(0.05)
ax.plot_surface(x,y,z, rstride=3, cstride=10,cmap=cm.coolwarm)
ax.set_xlabel('WOB Label')
ax.set_ylabel('RPM Label')
ax.set_zlabel('ROP Label')

n,m = 120,120
q,p = 0,0

best_ROP = 0

number_itr = 0
best_ROP_i = 0
i = 0
j = m/2
j = int(j)
itr_since_best_ROP = 0
new_best_ROP = False
while j < m:
    i = 0
    new_best_ROP = False
    itr_since_best_ROP = 0
    while i < n:
        number_itr +=1
        itr_since_best_ROP += 1
        #This possible implmentation does not garantee as good result, but number of itr reduce drastically
        if itr_since_best_ROP >5 and new_best_ROP == True:
            pass
           # break
        if z[j,i] > best_ROP:
            new_best_ROP = True
            itr_since_best_ROP = 0
            best_ROP = z[j,i]
            best_ROP_i = i
        i+=1
        
        #plt.plot([x[j,i-1]],[y[j,i-1]],[z[j,i-1]], markerfacecolor='r', markeredgecolor='k', marker='o', markersize=5, alpha=0.6)
        
    
    plt.plot([x[j,best_ROP_i]],[y[j,best_ROP_i]],[z[j,best_ROP_i]], markerfacecolor='k', markeredgecolor='k', marker='o', markersize=5, alpha=0.6)
    
    if z[j+1,best_ROP_i] > z[j,best_ROP_i]:
        j+=1
        
    elif z[j-1,best_ROP_i] > z[j,best_ROP_i]:
        j-=1
        
    else:
        print("Best ROP = " + str(z[j,best_ROP_i]) +(" with RPM = ")+ str(x[j,best_ROP_i]) +(" and WOB =  ")+ str(y[j,best_ROP_i]))
        break

plt.show()        
print("Number of itterations: " + str(number_itr))
        


