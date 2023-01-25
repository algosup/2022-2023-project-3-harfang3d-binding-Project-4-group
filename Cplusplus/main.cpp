#include <iostream>
#include <stdio.h>
#include "Vector3/Vector3.cpp"

// this file is used for testing. The vector library is located in vector.h.

using namespace std;

int main() {
    // C++ CODE

    Vector3 p3(0, 0, 4);
    printf("P3's coordinates are X:%f, Y:%f and Z:%f.\n", p3.x, p3.y, p3.z);

    Vector3 p4(0, 4, 0);
    printf("P4's coordinates are X:%f, Y:%f and Z:%f.\n", p4.x, p4.y, p4.z);

    Vector3 mp = p3.midpoint(p4);
    printf("The midpoint between points p1 and p2 is (%f, %f, %f).\n", mp.x, mp.y, mp.z);
    // add your tests above this line.
    

    return 0;
    
}