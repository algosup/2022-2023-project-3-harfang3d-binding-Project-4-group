// C++ library
#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>

class Vector2 {
public:
     Vector2(double inx = 0, double iny = 0) {
         x = inx;
         y = iny;
     }
    double x;
    double y;
    double distanceTo(Vector2 pos) {
        return sqrt((pos.y - y) * (pos.y - y) + (pos.x - x) * (pos.x - x));
    }
    void vectorMovement(double plusx, double plusy) {
        x += plusx;
        y += plusy;
        return;
    }
    Vector2 midpoint(Vector2 pos) {
        double mx = (x + pos.x) / 2;
        double my = (y + pos.y) / 2;
        Vector2 mid(mx, my);
        return mid;
    }
    //Calculate the distance between the vector and another vector in percents, like it was a 100% loading bar
    double percentDistance(Vector2 pos, double percentOfDistance = 100) {
        return distanceTo(pos) / (100 / percentOfDistance);
    }
};