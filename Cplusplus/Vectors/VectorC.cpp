#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>

extern "C" struct Vector2 {
    double x;
    double y;
};

extern "C" double distanceToV2(Vector2 pos, Vector2 end)
{
    return sqrt((pos.y - end.y) * (pos.y - end.y) + (pos.x - end.x) * (pos.x - end.x));
}

extern "C" Vector2 vectorMovementV2(Vector2 mov, double plusx, double plusy) {
    mov.x += plusx;
    mov.y += plusy;
    return mov;
}

extern "C" Vector2 midpointV2(Vector2 fst, Vector2 scd) {
        double mx = (fst.x + scd.x) / 2;
        double my = (fst.y + scd.y) / 2;
        Vector2 mid;
        mid.x = mx;
        mid.y = my;

        return mid;
}

extern "C" double percentDistanceV2(Vector2 pos, Vector2 end, double percentOfDistance = 100) {
        return distanceToV2(pos, end) / (100 / percentOfDistance);
    }

extern "C" struct Vector3 {
    double x;
    double y;
    double z;
};

extern "C" double distanceToV3(Vector3 pos, Vector3 end)
{
    return sqrt((pos.y - end.y) * (pos.y - end.y) + (pos.x - end.x) * (pos.x - end.x) + (pos.z - end.z) * (pos.z - end.z));
}

extern "C" Vector3 vectorMovementV3(Vector3 mov, double plusx, double plusy, double plusz) {
    mov.x += plusx;
    mov.y += plusy;
    mov.z += plusz;
    return mov;
}


extern "C" Vector3 midpointV3(Vector3 fst, Vector3 scd) {
        double mx = (fst.x + scd.x) / 2;
        double my = (fst.y + scd.y) / 2;
        double mz = (fst.z + scd.z) / 2;
        Vector3 mid;
        mid.x = mx;
        mid.y = my;
        mid.z = mz;

        return mid;
}

extern "C" double percentDistanceV3(Vector3 pos, Vector3 end, double percentOfDistance = 100) {
    return distanceToV3(pos, end) / (100 / percentOfDistance);
}