import numpy as np
from matplotlib import pyplot as plt
import matplotlib

print('Enter length and udl value of beam:\n');

# l =float(input())
# q = float(input())
l = 5 #m
q = 20 #Kn/m

x = np.linspace(0,5,20)
print(x)
M = q/2*(l*x-x**2)
V = q*(l/2 - x)
plt.figure(figsize=(10,4))
plt.plot([0]*len(x),color='k')
plt.locator_params(axis='x',nbins=40)
plt.locator_params(axis="y",nbins=20)
plt.xlabel('distance from one end')
plt.ylabel('values')
plt.title('Bending Moment and Shear Force')
y= np.arange(0,20,1)
print(y)
x_point = [round(num, 1) for num in x]
plt.xticks(y,x_point)


plt.plot(-M)
plt.plot(V)
plt.show()


