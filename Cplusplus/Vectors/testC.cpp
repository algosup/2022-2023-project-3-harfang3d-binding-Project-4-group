#include <iostream>
#include <stdio.h>
#include "VectorC.cpp"

// this file is used for testing. The vector library is located in vector.h.

using namespace std;

int main() {
    // C CODE

    struct Vector2 p1;
    struct Vector2 p2; 

    p1.x = 0;
    p1.y = 0;

    p2.x = 0;
    p2.y = 100;

    printf("P1 x is equal to: %d\n", p1.x);

    double distance = distanceToV2(p1, p2);
    printf("The distance between points p1 and p2 is %f.\n", distance);

    p1 = vectorMovementV2(p1, 2, 2);
    printf("P1's new coordinates are X: %f and Y: %f. \n", p1.x, p1.y);

    Vector2 midP1_P2 = midpointV2(p1, p2);
    printf("P1 and P2's midpoint's coordinates are X: %f and Y: %f. \n ", midP1_P2.x, midP1_P2.y);

    double distancePercent = percentDistanceV2(p1, p2);
    printf("The distance between points p1 and p2 is %f%. \n ", distancePercent);

    struct Vector3 p3;
    struct Vector3 p4; 

    p3.x = 0;
    p3.y = 0;
    p3.z = 4;

    p4.x = 0;
    p4.y = 4;
    p4.z = 0;

    printf("P3's coordinates are X:%f, Y:%f and Z:%f.\n", p3.x, p3.y, p3.z);

    printf("P4's coordinates are X:%f, Y:%f and Z:%f.\n", p4.x, p4.y, p4.z);

    Vector3 midP3_P4 = midpointV3(p3, p4);
    printf("The midpoint between points p3 and p4 is (%f, %f, %f).\n", midP3_P4.x, midP3_P4.y, midP3_P4.z);

    double distance = distanceToV3(p3, p4);
    printf("The distance between points p3 and p4 is %f.\n", distance);

    p3 = vectorMovementV3(p3, 2, 2, 2);
    printf("P3's new coordinates are X: %f , Y: %f and Z: %f. \n ", p3.x, p3.y, p3.z);

    double distancePercent = percentDistanceV3(p3, p4);
    printf("The distance between points p1 and p2 is %f%. \n ", distancePercent);

    return 0;
}