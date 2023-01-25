#include <iostream>
#include <stdio.h>
#include "Vector2.cpp"

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

    return 0;
}