#include "Original.h"
#include <stdio.h>
#include <iostream>

int main(){
    return 0;
}
class vectest{
        public:
        double X;
        double Y;
        vectest(double x, double y) : X(x), Y(y){}
};
extern "C" vectest* Create(double x, double y){
        printf("before x= %f and y=%f\n",x,y);
        double X=x;
        double Y=y;
        printf("after x= %f and y=%f\n",X,Y);

        return  new vectest(X,Y);
};
extern "C" double* distanceTo(Vector2* v1, Vector2* v2){
        // Vector2 vec1(v1->x,v1->y);
        // Vector2 vec2(v2->x,v2->y);
        printf("%lu\n",sizeof(v1->x));
        // printf("%f,%f",v2->x,v2->y);
        // double result= vec1.distanceTo(vec2);
        return new double(0.0);
};
extern "C" double* test(double x){
        return new double(x);
};
