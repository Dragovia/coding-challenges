#include <bits/stdc++.h>
#include <iostream>

using namespace std;

///creating a node
class Node {
public:
    int value;
    Node* next;

};

int main(){

    Node* head;
    Node* one = NULL;
    Node* two = NULL;
    Node* three = NULL;

    ///allocate 3 nodes into the heap

    one = new Node();
    two = new Node();
    three = new Node();

    ///Assign value values
    one -> value = 1;
    two -> value = 2;
    three -> value = 3;

    ///connect nodes

    one->next = two;
    two->next = three;
    three->next = NULL;

    ///
    head = one;

    while(head!= NULL){
    //    cout << head->value;
        head = head->next;
    }
        cout << "one " << one -> value <<" " << &one;
        cout <<endl;
    cout << "two " << two -> value <<" " << &two;
    cout <<endl;
        cout << "three " << three -> value <<" " << &three;



}
