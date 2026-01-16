#include "iostream"
#include "utility"
#include "string"
#include "tuple"
using namespace std;
int main(){ 
    cout << "Hello world" << endl;
    pair<int,int> a = {1,2};
    // cout << a << endl; 
    cout << a.first << " AND " << a.second << endl;

    // Pair inside pair : 
    pair<int, pair<int,string>> stuff = {1, {1, "Apple"}};
    // cout << stuff.second << endl; // This won't work. 
    cout << stuff.first << ":" << stuff.second.first << "," << stuff.second.second << endl;
    // array of pairs : 
    pair<int, int> pair_list[] = {
        {1,2}, 
        {3,4}, 
        {5,6},
        {7,8}
    };
    cout << sizeof(pair_list) << endl; // Shows the memory size, i.e, 32!!!
    //Here is the right way : 
    int _pair_size = sizeof(pair_list) / sizeof(pair_list[0]);
    cout << _pair_size << endl; 

    for (int i = 0; i < _pair_size; i++){
        cout << pair_list[i].first << ":" << pair_list[i].second << endl;
        cout << "Bingo!" << endl;
    }
    return 0; 

}