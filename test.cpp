#include <iostream>
using namespace std;

int b1(int x, int y){
    return x+y;
}

int main(){
    int a1 = 10;
    int *a = &a1;
    int (*f)(int, int) = b1;
    int result = f(5, 6);
    cout<<(*a)<<endl;
    cout<<result<<endl;
}
