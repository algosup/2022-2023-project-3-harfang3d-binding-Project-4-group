#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>

extern "C" class Vector2 {
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
};

Vector2 vector2(double inx, double iny) {
    return Vector2(inx, iny);
}
