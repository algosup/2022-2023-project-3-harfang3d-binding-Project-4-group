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