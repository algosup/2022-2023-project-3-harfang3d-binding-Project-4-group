#include <math.h>
#include <iostream>
using namespace std;
int main() 
{
   return 0;
}
class Vector3
{
public:
double X;
double Y;
double Z;
Vector3(double x, double y, double z) : X(x), Y(y), Z(z) {}
};
extern "C" Vector3* CreateVector3(double x, double y, double z)
{
return new Vector3(x, y, z);
}
extern "C" double GetX(Vector3 *v)
{
return v->X;
}
extern "C" double GetY(Vector3 *v)
{
return v->Y;
}
extern "C" double GetZ(Vector3 *v)
{
return v->Z;
}
extern "C" double distanceTo(Vector3 *pos1, Vector3 *pos2)
{
return sqrt((pos1->Y - pos2->Y) * (pos1->Y - pos2->Y) + (pos1->X - pos2->X) * (pos1->X - pos2->X) + (pos1->Z - pos2->Z) * (pos1->Z - pos2->Z));
}
extern "C" void vectorMovement(Vector3* vector, double plusx, double plusy, double plusz)
{
vector->X += plusx;
vector->Y += plusy;
vector->Z += plusz;
return;
}
extern "C" Vector3 *midpoint(Vector3* pos1, Vector3* pos2)
{
double mx = (pos1->X + pos2->X) / 2; 
double my = (pos1->Y + pos2->Y) / 2; 
double mz = (pos1->Z + pos2->Z) / 2; 
return CreateVector3(mx, my, mz);
}
extern "C" double percentDistance(Vector3* pos,Vector3* pos2, double percentOfDistance) {
return distanceTo(pos,pos2)/ (100 / percentOfDistance);
}