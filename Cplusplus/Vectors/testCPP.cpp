#include <iostream>
#include <stdio.h>
#include "VectorCPP.cpp"

// this file is used for testing. The vector library is located in vector.h.

using namespace std;

int main() {    
    //C++ CODE

    Vector2 p1(0, 0);
    Vector2 p2(0, 100);

    cout << "P1 x is equal to: " <<p1.x << "\n"; 

    double distance = p1.distanceTo(p2);
    printf("The distance between points p1 and p2 is %f.\n", distance);

    p1.vectorMovement(2, 2);
    printf("P1's new coordinates are X: %f and Y: %f. \n ", p1.x, p1.y);

    Vector2 midP1_P2 = p1.midpoint(p2);
    printf("P1 and P2's midpoint's coordinates are X: %f and Y: %f. \n ", midP1_P2.x, midP1_P2.y);

    double distancePercent = p1.percentDistance(p2);
    printf("The distance between points p1 and p2 is %f%. \n ", distancePercent);

    Vector3 p3(0, 0, 4);
    printf("P3's coordinates are X:%f, Y:%f and Z:%f.\n", p3.x, p3.y, p3.z);

    Vector3 p4(0, 4, 0);
    printf("P4's coordinates are X:%f, Y:%f and Z:%f.\n", p4.x, p4.y, p4.z);

    Vector3 mp = p3.midpoint(p4);
    printf("The midpoint between points p3 and p4 is (%f, %f, %f).\n", mp.x, mp.y, mp.z);

    double distance = p3.distanceTo(p4);
    printf("The distance between points p3 and p2 is %f.\n", distance);

    p3.vectorMovement(2, 2, 2);
    printf("P3's new coordinates are X: %f , Y: %f and Z: %f. \n ", p3.x, p3.y, p3.z);

    double distancePercent = p3.percentDistance(p4);
    printf("The distance between points p3 and p4 is %f%. \n ", distancePercent);

    return 0;
}