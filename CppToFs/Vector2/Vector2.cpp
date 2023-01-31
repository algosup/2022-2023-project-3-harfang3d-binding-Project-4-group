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
extern "C" Vector2* CreateVector2(double x, double y) {
  return new Vector2(x, y);
}

extern "C" double GetX(Vector2* v) {
  return v->X;
}

extern "C" double GetY(Vector2* v) {
  return v->Y;
}
extern "C" double distanceTo(Vector2* pos1,Vector2* pos2) {

        return sqrt(pow(pos2->X - pos1->X,2) + pow(pos2->Y - pos1->Y,2) );
    }
extern "C" void vectorMovement(Vector2* vector,double plusx, double plusy) {
    vector->X += plusx;
    vector->Y += plusy;
    return;
}
extern "C" Vector2* midpoint(Vector2* pos1, Vector2* pos2) {
    double mx = (pos1->X + pos2->X) / 2;
    double my = (pos1->Y + pos2->Y) / 2;
    return new Vector2 (mx, my);
}
extern "C" double percentDistance(Vector2* pos,Vector2* pos2, double percentOfDistance) {
        return distanceTo(pos,pos2)/ (100 / percentOfDistance);
    }