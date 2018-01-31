#MAKEFILE for Propogator routine
#
#Steven Large
#January 14th 2018

PRODUCT_NEQ = NoneqPropogator.exe
PRODUCT_EQ = EquilibriumSampling.exe

ODIR = obj
LDIR = lib
IDIR = include
SDIR = src

MAINFILE_NEQ = $(SDIR)/Driver.cpp
MAINFILE_EQ = $(SDIR)/EquilibriumSampling.cpp

SOURCES_NEQ = $(SDIR)/Propogator.cpp
OBJECTS_NEQ = $(SDIR)/$(ODIR)/Propogator.o

SOURCES_EQ = $(SDIR)/Propogator.cpp
LIBRARIES_EQ = $(LDIR)/TrajectoryTracking.cpp
OBJECTS_EQ = $(SDIR)/$(ODIR)/TrajectoryTracking.o

CFLAGS = -I.

DEPS_NEQ = $(IDIR)/DiscreteControl.h
DEPS_EQ = $(IDIR)/DiscreteControl.h $(IDIR)/DiscreteControl_Eq.h

CC = g++ -O3


all: $(PRODUCT_NEQ) $(PRODUCT_EQ)

$(OBJECTS_NEQ): $(SOURCES_NEQ)
	$(CC) -c $(SOURCES_NEQ) -o $(OBJECTS_NEQ) $(CFLAGS) 

$(OBJECTS_EQ): $(SOURCES_EQ)
	$(CC) -c $(SOURCES_EQ) -o $(OBJECTS_EQ) $(CFLAGS)

$(PRODUCT_NEQ): $(MAINFILE_NEQ) $(OBJECTS_NEQ) $(DEPS_NEQ)
	$(CC) $(MAINFILE_NEQ) $(OBJECTS_NEQ) -o $(PRODUCT_NEQ) $(CFLAGS)

$(PRODUCT_EQ): $(MAINFILE_EQ) $(OBJECTS_EQ) $(DEPS_EQ)
	$(CC) $(MAINFILE_EQ) $(OBJECTS_EQ) -o $(PRODUCT_EQ) $(CFLAGS)



clean:
	rm -f $(SDIR)/$(ODIR)/*.o

