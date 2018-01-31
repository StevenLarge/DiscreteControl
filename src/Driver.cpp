/* Equilibrium Sampling Driver Implementation written in C++ with a Correlation function calculator built in */

#include <fstream>
#include <iostream>
#include <random>
#include <cmath>
#include <string>
#include <ctime>

//#include "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/lib/DiscreteControl.h"

#include "include/DiscreteControl.h"
#include "include/ReadWrite.h"

using namespace std;



int main(){

	HelloWorld(1);

	string ImportName = "Protocols/Naive_Steps_160_Time_1000.000000.dat"

	double * CPVals;
	double * LagTime;
	CPVals = new double [160];
	LagTime = new double [160];

	ImportProtocol(CPVals,LagTime,ImportName)


}


