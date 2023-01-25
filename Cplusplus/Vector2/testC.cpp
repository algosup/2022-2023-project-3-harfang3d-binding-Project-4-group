#include <iostream>
#include <stdio.h>
#include "Vector2C.cpp"

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

    double distance = distanceTo(p1, p2);
    printf("The distance between points p1 and p2 is %f.\n", distance);

    p1 = vectorMovement(p1, 2, 2);
    printf("P1's new coordinates are X: %f and Y: %f. \n", p1.x, p1.y);

    Vector2 midP1_P2 = midpoint(p1, p2);
    printf("P1 and P2's midpoint's coordinates are X: %f and Y: %f. \n ", midP1_P2.x, midP1_P2.y);

    double distancePercent = percentDistance(p1, p2);
    printf("The distance between points p1 and p2 is %f%. \n ", distancePercent);

    return 0;
}