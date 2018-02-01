#This is prototype optimization code written in Python for the restricted optimization of time allocation and/or spatial optimization in a discrete protocol
#
#Steven Large
#January 30th 2018

import os
import math
import random

import matplotlib.pyplot as plt
import numpy as np


def ImportCorrelationMesh(Path,Filename):

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


def TangentPlane(CPTimes):




def CalculateCost(CPTimes,CPVals,CorrelationMatrix):



def ComputeGradient(CPVals,CPTime,CorrelationMatrix):

	GradientVector = []

	#Find Gradient along each of the CP Time directions

	#Find the total gradient vector

	return GradientVector


def RestrictionUpdate(VectorGradient,StepSize,CorrelationMatrix,CPVals,CPTimes):

	NewCPTimes = []

	#Project Gradient vector onto Tangent space

	#Increment the current protocol times in the tangent space

	#Project the incremented point back onto the N-1 Sphere

	return NewCPTimes


def OptimizeTime(NumSteps,TotalTime,CPVals):

	NaiveTime = float(NumSteps)/float(TotalTime)

	StepTime = []
	InitialTime = []

	Iterations = 1000

	CostTracker = []

	StepSize = 0.1

	CorrelationMatrix = ImportCorrelationMesh(Path,Filename)

	for index in range(NumSteps - 1):

		StepTime.append(NaiveTime)
		InitialTime.appen(NaiveTime)

	CostTracker.append(CalculateCost(StepTime,CPVals,CorrelationMatrix))

	for index in range(len(Iterations)):

		VectorGradient = ComputeGradient(CPVals,StepTime,CorrelationMatrix)

		StepTime = RestrictionUpdate(VectorGradient,StepSize,CorrelationMatrix,CPVals,StepTime)

		CostTracker.append(CalculateCost(StepTime,CPVals,CorrelationMatrix))

	plt.plot(NaiveTime,CPVals,'o')
	plt.plot(StepTime,CPVals,'o')
	plt.show()
	plt.close()





