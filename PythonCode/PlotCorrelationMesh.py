#This python script plots the correlation mesh and heat map for equilibrium data
#
#Steven Large
#January 31st 2018

import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
from math import *


def ReadArray(Path,Filename):

	CompleteName = os.path.join(Path,Filename)

	CorrelationArray = []

	file1 = open(CompleteName,'r')
	TotalData = file1.readlines()
	file1.close()

	for index1 in range(len(TotalData)):
		Parsed = TotalData[index1].split()
		CorrelationArray.append([])
		for index2 in range(len(Parsed)):
			CorrelationArray[index1].append(eval(Parsed[index2]))

	return CorrelationArray


def ReadVector(Path,Filename):

	CompleteName = os.path.join(Path,Filename)

	Data = []

	file1 = open(CompleteName,'r')
	TempData = file1.readlines()
	file1.close()

	for index in range(len(TempData)):
		Parsed = TempData[index].split()
		Data.append(eval(Parsed[0]))

	return Data


def PlotHeatMap(CorrArray,LagTime,CPVals):

	LagTimeNP = np.zeros(int(len(LagTime)/2))
	CPValsNP = np.zeros(len(CPVals))

	#print("Check 1 --- \n\n")

	for index in range(int(len(LagTime)/2)):
		LagTimeNP[index] = LagTime[index]

	#print("Check 2 --- \n\n")

	for index in range(len(CPVals)):
		CPValsNP[index] = CPVals[index]

	#print("Check 3 --- \n\n")

	CorrMeshNP = np.zeros((len(CorrArray),int(len(CorrArray[0])/2)))

	#print("Check 4 --- \n\n")

	for index1 in range(len(CorrArray)):
		for index2 in range(int(len(CorrArray[0])/2)):
			CorrMeshNP[index1,index2] = CorrArray[index1][index2]

	#print("Check 5 --- \n\n")

	LagTimeNP,CPValsNP = np.meshgrid(LagTimeNP,CPValsNP)

	#print("Check 6 --- \n\n")

	#print np.shape(LagTimeNP)
	#print np.shape(CPValsNP)
	#print np.shape(CorrMeshNP)

	hfont = {'fontname':'Times New Roman'}

	plt.imshow(CorrMeshNP, cmap='plasma', interpolation='nearest', aspect='auto')
	plt.colorbar()
	plt.xlabel("Lag Time", fontsize=18, **hfont)
	plt.ylabel("Control Parameter", fontsize=18, **hfont)
	plt.savefig("Plots/AutoCorrHeatMap.png", format='png')
	#plt.show()
	plt.close()



def PlotCorrSurface(CorrArray,LagTime,CPVals):

	LagTimeNP = np.zeros(int(len(LagTime)/2))
	CPValsNP = np.zeros(len(CPVals))

	#print("Check 1 --- \n\n")

	for index in range(int(len(LagTime)/2)):
		LagTimeNP[index] = LagTime[index]

	#print("Check 2 --- \n\n")

	for index in range(len(CPVals)):
		CPValsNP[index] = CPVals[index]

	#print("Check 3 --- \n\n")

	CorrMeshNP = np.zeros((len(CorrArray),int(len(CorrArray[0])/2)))

	#print("Check 4 --- \n\n")

	for index1 in range(len(CorrArray)):
		for index2 in range(int(len(CorrArray[0])/2)):
			CorrMeshNP[index1,index2] = CorrArray[index1][index2]

	#print("Check 5 --- \n\n")

	LagTimeNP,CPValsNP = np.meshgrid(LagTimeNP,CPValsNP)

	#print("Check 6 --- \n\n")

	#print np.shape(LagTimeNP)
	#print np.shape(CPValsNP)
	#print np.shape(CorrMeshNP)

	fig = plt.figure()
	ax = Axes3D(fig)
	ax.plot_surface(LagTimeNP,CPValsNP,CorrMeshNP, rstride=1, cstride=1, cmap='plasma')

	hfont = {'fontname':'Times New Roman'}

	ax.text2D(0.30,0.95, "Autocorrelation Mesh", transform=ax.transAxes, fontsize=20, **hfont)

	ax.set_xlim(0,250)
	ax.set_ylim(-1,1)
	ax.set_zlim(0,3.5)
	ax.set_xlabel('Lag Time', fontsize=16, **hfont)
	ax.set_ylabel('Trap Minima', fontsize=16, **hfont)
	ax.set_zlabel('Force Autocorrelation', fontsize=16, **hfont)
	plt.savefig('Plots/AutoCorrMesh.png',format='png')
	#plt.show()
	plt.close()




ReadPath = "CorrelationMesh/"
WritePath = "Plots/"

ReadNameArray = "CorrelationMesh.dat"
ReadNameTime = "LagTime.dat"
ReadNameCP = "CPVals.dat"

CorrArray = ReadArray(ReadPath,ReadNameArray)
LagTime = ReadVector(ReadPath,ReadNameTime)
CPVals = ReadVector(ReadPath,ReadNameCP)

PlotHeatMap(CorrArray,LagTime,CPVals)
PlotCorrSurface(CorrArray,LagTime,CPVals)











