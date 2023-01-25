#include <iostream>
using namespace std;

int main(){
    cout << "test";
    return 0;
}
class MyClass {
    private:
    int value;

    public:
    MyClass() {
        value = 0;
    }

    int getValue() {
        return value;
    }

    void setValue(int newValue) {
        value = newValue;
    }
};

extern "C" {
    MyClass* MyClass_Create() {
        return new MyClass();
    }

    int MyClass_getValue(MyClass* myClass) {
        return myClass->getValue();
    }

    void MyClass_setValue(MyClass* myClass, int newValue) {
        myClass->setValue(newValue);
    }

    void MyClass_destroy(MyClass* myClass) {
        delete myClass;
    }
}

