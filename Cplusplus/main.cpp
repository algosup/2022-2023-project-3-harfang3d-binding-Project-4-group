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
    p1.y = 1;

    p2.x = 2;
    p2.y = 0;

    printf("P1 x is equal to: %d\n", p1.x);

    double distance = distanceTo(p1, p2);

    printf("The distance between points p1 and p2 is %f.\n\n", distance);

    //C++ CODE

    // Vector2 p1(0, 1);
    // Vector2 p2(2, 0);

    // cout << "P1 x is equal to: " <<p1.x << "\n"; 

    // double distance = p1.distanceTo(p2);
    // printf("The distance between points p1 and p2 is %f.\n\n", distance);
    //printf("Testing finished, press enter to exit.");
    //cin.get();
    return 0;
}