#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>

extern "C" struct Vector3 {
    double x;
    double y;
    double z;
};

extern "C" Vector3 midpoint(Vector3 fst, Vector3 scd) {
        double mx = (fst.x + scd.x) / 2;
        double my = (fst.y + scd.y) / 2;
        double mz = (fst.z + scd.z) / 2;
        Vector3 mid;
        mid.x = mx;
        mid.y = my;
        mid.z = mz;

        return mid;
}