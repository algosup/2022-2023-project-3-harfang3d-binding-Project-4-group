#include <iostream>
#include <stdio.h>
#include "Vector2.cpp"

// this file is used for testing. The vector library is located in vector.h.

using namespace std;

int main() {
    Vector2 p1(0, 4);
    Vector2 p2(4, 0);
    double distance = p1.distanceTo(p2);
    printf("The distance between points p1 and p2 is %f.\n\n", distance);
    printf("Testing finished, press enter to exit.");
    cin.get();
    return 0;
}