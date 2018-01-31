/* This is a header file for the Discrete Control Nonequilbrium simulations */


/* Global variable declarations */

extern double dt;
extern double CPMax;
extern double CP;
extern int MAXLAG;
extern double EqTime;
extern int TotalStats;
extern double dX;


/* Propogator routines */

void HelloWorld(int a);

void LangevinBistable(double * position, double * velocity, double * time);
void Langevin(double * position, double * velocity, double * time);

double ForceParticleTrap(double position);
double ForceParticleBistable(double position);
double ForceParticleBistableTrap(double position);
double BistableWell(double position);
