#include "iostream"
#include "vector"
using namespace std; 

// Struct for a Node
struct Node {
    public:
    int data;
    Node* next; 
    // Node (int data1, Node* next1){
    //     data = data1;
    //     next = next1; 
    // }
    Node (int data1, Node* next1) : data(data1), next(next1) {}
};

// function to convert an array to linkedlist 
Node* Arr2LL(
    const vector<int> &arr
){
    if (arr.empty()) return nullptr;
    
    Node* head = new Node(arr[0], nullptr);
    Node *tail = head; 

    for (int i = 1; i < arr.size(); i++){
        tail.next = new Node(arr[i], nullptr);
        tail = tail.next; 
    }

    return head; 
}

int main(){
    Node first = Node(10,nullptr);
    cout << first.data<< endl;
    Arr2LL(vector<int> {1,2});
    return 0;
}