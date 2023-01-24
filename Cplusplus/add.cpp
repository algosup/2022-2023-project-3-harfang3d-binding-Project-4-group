#include <iostream>

extern "C" int add(int a, int b) {
    return a + b;
}

//extern "C" add(1, 2);

 extern "C" int main() {
     add(1, 2);
 }