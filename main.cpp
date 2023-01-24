#include <iostream>
#include <stdio.h>
#include "vector.h"

// this file is used for testing. The vector library is located in vector.h.

using namespace std;

int main() {
    Vector2 p1(0, 4);
    Vector2 p2(4, 0);
    double distance = p1.distanceTo(p2);
    printf("The distance between points p1 and p2 is %f.\n\n", distance);
    Vector3 p3(0, 0, 4);
    Vector3 p4(0, 4, 0);
    Vector3 mp = p3.midpoint(p4);
    printf("The midpoint between points p1 and p2 is (%f, %f, %f).\n\n", mp.x, mp.y, mp.z);
    // add your tests above this line.
    printf("Testing finished, press enter to exit.");
    cin.get();
    return 0;
}
