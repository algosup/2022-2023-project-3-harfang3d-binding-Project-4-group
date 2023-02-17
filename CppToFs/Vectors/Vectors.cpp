#include <math.h>
#include <iostream>
#include "Vector.h"
using namespace std;
int main()
{
   return 0;
}

extern "C" Vector2 *CreateVector2D(double x, double y)
{
   return new Vector2(x, y);
}
extern "C" double distanceTo2D(Vector2* pos1, Vector2* pos2)
{   
   return pos1->distanceTo(*pos2);
}
extern "C" void vectorMovement2D(Vector2* vector, double plusx, double plusy)
{
   vector->vectorMovement(plusx, plusy);
   return;
}
extern "C" Vector2 *midpoint2D(Vector2* pos1, Vector2* pos2)
{
   return new Vector2(pos1->midpoint(*pos2));
}
extern "C" double percentDistance2D(Vector2* pos, Vector2* pos2, double percentOfDistance)
{
   return pos->percentDistance(*pos2, percentOfDistance);
}



extern "C" Vector3 *CreateVector3D(double x, double y,double z)
{
   return new Vector3(x, y, z);
}
extern "C" double distanceTo3D(Vector3* pos1, Vector3* pos2)
{   
   return pos1->distanceTo(*pos2);
}
extern "C" void vectorMovement3D(Vector3* vector, double plusx, double plusy, double plusz)
{
   vector->vectorMovement(plusx, plusy, plusz);
   return;
}
extern "C" Vector3 *midpoint3D(Vector3* pos1, Vector3* pos2)
{
   return new Vector3(pos1->midpoint(*pos2));
}
extern "C" double percentDistance3D(Vector3* pos, Vector3* pos2, double percentOfDistance)
{
   return pos->percentDistance(*pos2, percentOfDistance);
}
