#This script generates the parameters for a double exponential eacy function for the bistabel stationary autocorrelation functions
#
#Steven Large
#February 6th 2017

import os

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def Function(x,a,b,c,d):

	return a*np.exp(-b*x) + c*np.exp(-d*x)

def Driver(xData,yData):

	xData_NP = np.asarray(xData)
	yData_NP = np.asarray(yData)

	popt,pcov = curve_fit(Function,xData_NP,yData_NP,bounds=(0,100))

	return popt












