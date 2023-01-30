#include <iostream>
#include <stdio.h>
#include "Vectors/VectorCPP.cpp"

// this file is used for testing. The vector library is located in vector.h.

using namespace std;

int main() {
    // C CODE

    // struct Vector3 p3;
    // struct Vector3 p4; 

    // p3.x = 0;
    // p3.y = 0;
    // p3.z = 4;

    // p4.x = 0;
    // p4.y = 4;
    // p4.z = 0;

    // printf("P3's coordinates are X:%f, Y:%f and Z:%f.\n", p3.x, p3.y, p3.z);

    // printf("P4's coordinates are X:%f, Y:%f and Z:%f.\n", p4.x, p4.y, p4.z);

    // Vector3 midP3_P4 = midpointV3(p3, p4);
    // printf("The midpoint between points p3 and p4 is (%f, %f, %f).\n", midP3_P4.x, midP3_P4.y, midP3_P4.z);

    // double distance = distanceToV3(p3, p4);
    // printf("The distance between points p3 and p4 is %f.\n", distance);

    // p3 = vectorMovementV3(p3, 2, 2, 2);
    // printf("P3's new coordinates are X: %f , Y: %f and Z: %f. \n ", p3.x, p3.y, p3.z);

    // double distancePercent = percentDistanceV3(p3, p4);
    // printf("The distance between points p1 and p2 is %f%. \n ", distancePercent);

    // C++ CODE

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