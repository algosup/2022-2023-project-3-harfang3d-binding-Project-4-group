#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>

extern "C" struct Vector2 {
    double x;
    double y;
};

extern "C" double distanceTo(Vector2 pos, Vector2 end)
{
        return sqrt((pos.y - end.y) * (pos.y - end.y) + (pos.x - end.x) * (pos.x - end.x));
}

extern "C" Vector2 vectorMovement(Vector2 mov, double plusx, double plusy) {
    mov.x += plusx;
    mov.y += plusy;
    return mov;
}

 extern "C" Vector2 midpoint(Vector2 fst, Vector2 scd) {
        double mx = (fst.x + scd.x) / 2;
        double my = (fst.y + scd.y) / 2;
        Vector2 mid;
        mid.x = mx;
        mid.y = my;

        return mid;
}