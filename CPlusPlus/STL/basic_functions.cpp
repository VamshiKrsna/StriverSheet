#include "iostream"
using namespace std;
void greet(); 
int sum(int a, int b){
    return a+b;
}

int main(){
    greet();
    cout << sum(10,20);
    return 0; 
}

void greet(){
    cout << "Hello There!";
}