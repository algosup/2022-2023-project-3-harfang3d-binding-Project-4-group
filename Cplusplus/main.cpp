#include <iostream>
#include <stdio.h>
//#include "Vector2.cpp"
#include "Vector2C.cpp"

// this file is used for testing. The vector library is located in vector.h.

using namespace std;

int main() {
    // C++ CODE

    Vector3 p3(0, 0, 4);
    Vector3 p4(0, 4, 0);
    Vector3 mp = p3.midpoint(p4);
    printf("The midpoint between points p1 and p2 is (%f, %f, %f).\n\n", mp.x, mp.y, mp.z);
    // add your tests above this line.
    printf("Testing finished, press enter to exit.");
    cin.get();
    return 0;
    
}