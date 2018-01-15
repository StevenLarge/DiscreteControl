#MAKEFILE for Propogator routine
#
#Steven Large
#January 14th 2018

PRODUCT = NoneqPropogator.exe

ODIR = obj
LDIR = lib
IDIR = include
SDIR = src

MAINFILE = $(SDIR)/Driver.cpp

SOURCES = $(SDIR)/Propogator.cpp
OBJECTS = $(SDIR)/$(ODIR)/Propogator.o

CFLAGS = -I.
DEPS = $(IDIR)/DiscreteControl.h

CC = g++ -O3


all: $(PRODUCT)

$(OBJECTS): $(SOURCES)
	$(CC) -c $(SOURCES) -o $(OBJECTS) $(CFLAGS) 

$(PRODUCT): $(MAINFILE) $(OBJECTS) $(DEPS)
	$(CC) $(MAINFILE) $(OBJECTS) -o $(PRODUCT) $(CFLAGS)


clean:
	rm -f $(SDIR)/$(ODIR)/*.o

