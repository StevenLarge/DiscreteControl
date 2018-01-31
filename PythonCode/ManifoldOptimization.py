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


def CalculateCost(CPTimes,CPVals,CorrelationMatrix):


def ComputeGradient(CPVals,CPTime,CorrelationMatrix):


def RestrictionUpdate(VectorGradient,StepSize,CorrelationMatrix,CPVals,CPTimes)



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





