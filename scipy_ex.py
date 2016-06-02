'''this is a scipy example, where we use curve fit to fit a curve and plot the results'''
#lets play with scipy!
import numpy as np
import matplotlib as plt
from scipy.optimize import curve_fit
def func(x, a, b, c): 
    '''this returns an array (e^?) on x. 
    where x is the element by element array. a, b, c, are just constants of the function'''
    return a * np.exp(-b * x) + c
xdata = np.linspace( 0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
ydata = y + 8.2 * np.random.normal(size=len(xdata))
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(xdata,ydata, marker='*')
plt.plot(xdata, y)
plt.plot(xdata, func(xdata, popt[0], popt[1], popt[2]), marker='o')
