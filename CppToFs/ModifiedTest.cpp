#include <math.h>
#include <iostream>
using namespace std;

int main(){
    return 0;
}
class Vector2 {
  public:
    double X;
    double Y;
    Vector2(double x, double y) : X(x), Y(y) {}
};
 class Vector3 {
  public:
    double X;
    double Y;
    double Z;
    Vector3(double x, double y,double z) : X(x), Y(y) {}
};

extern "C" Vector2* CreateVector2(double x, double y) {
  return new Vector2(x, y);
}

extern "C" double GetX(Vector2* v) {
  return v->X;
}

extern "C" double GetY(Vector2* v) {
  return v->Y;
}
extern "C" double V2distanceTo(Vector2* pos1,Vector2* pos2) {

        return sqrt(pow(pos2->X - pos1->X,2) + pow(pos2->Y - pos1->Y,2) );
    }
// extern "C" void vectorMovement(Vector2* vector,double plusx, double plusy) {
//     vector->X += plusx;
//     vector->Y += plusy;
//     return;
// }
// extern "C" Vector2 midpoint(Vector2* pos1, Vector2* pos2) {
//     double mx = (pos1->X + pos2->Y) / 2;
//     double my = (pos1->X + pos2->Y) / 2;
//     Vector2 mid(mx, my);
//     return mid;
// }