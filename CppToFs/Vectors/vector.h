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
    double percentDistance(Vector2 pos, double percentOfDistance = 100) {
        return distanceTo(pos) / (100 / percentOfDistance);
    }
};
class Vector3 {
public:
    Vector3(double inx = 0, double iny = 0, double inz = 0) {
        x = inx;
        y = iny;
        z = inz;
    }
    double x;
    double y;
    double z;
    double distanceTo(Vector3 pos) {
        return sqrt((pos.y - y) * (pos.y - y) + (pos.x - x) * (pos.x - x) + (pos.z - z) * (pos.z - z));
    }
    void vectorMovement(double plusx, double plusy, double plusz) {
        x += plusx;
        y += plusy;
        z += plusz;
        return;
    }
    Vector3 midpoint(Vector3 pos) {
        double mx = (x + pos.x) / 2;
        double my = (y + pos.y) / 2;
        double mz = (z + pos.z) / 2;
        Vector3 mid(mx, my, mz);
        return mid;
    }
    double percentDistance(Vector3 pos, double percentOfDistance = 100) {
        return distanceTo(pos) / (100 / percentOfDistance);
    }
};
