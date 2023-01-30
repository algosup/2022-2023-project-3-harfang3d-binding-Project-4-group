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

extern "C" double distanceTo(Vector3 pos, Vector3 end)
{
    return sqrt((pos.y - end.y) * (pos.y - end.y) + (pos.x - end.x) * (pos.x - end.x) + (pos.z - end.z) * (pos.z - end.z));
}

// extern "C" Vector2 vectorMovement(Vector2 mov, double plusx, double plusy) {
//     mov.x += plusx;
//     mov.y += plusy;
//     return mov;
// }


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

// extern "C" double percentDistance(Vector2 pos, Vector2 end, double percentOfDistance = 100) {
//         return distanceTo(pos, end) / (100 / percentOfDistance);
//     }