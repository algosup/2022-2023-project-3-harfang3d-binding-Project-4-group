// C++ library
#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>

// class Vector2 {
// public:
//     Vector2(double inx = 0, double iny = 0) {
//         x = inx;
//         y = iny;
//     }
//     double x;
//     double y;
//     double distanceTo(Vector2 pos) {
//         return sqrt((pos.y - y) * (pos.y - y) + (pos.x - x) * (pos.x - x));
//     }
//     void vectorMovement(double plusx, double plusy) {
//         x += plusx;
//         y += plusy;
//         return;
//     }
//     Vector2 midpoint(Vector2 pos) {
//         double mx = (x + pos.x) / 2;
//         double my = (y + pos.y) / 2;
//         Vector2 mid(mx, my);
//         return mid;
//     }
//     double percentDistance(Vector2 pos, double percentOfDistance = 100) {
//         return distanceTo(pos) / (100 / percentOfDistance);
//     }
// };

 extern "C" struct Vector2 {
     double x = 0;
     double y =0;
 };

extern "C" Vector2 *Vector2_Constructor(Vector2 *this_ptr, int x);

extern "C" void vectorMovement(Vector2* vec2, double plusx, double plusy)
{
    &vec2.x += plusx;
    &vec2.y += plusy;
    return;
}

extern "C" Vector2 midpoint(Vector2* vec2, Vector2 pos)
{
   double mx = (&vec2.x + pos.x) / 2;
   double my = (&vec2.y + pos.y) / 2;
   Vector2 mid(mx, my);
   return mid;
}