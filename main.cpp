#include <iostream>
#include <stack>

using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int value) : data(value), left(nullptr), right(nullptr) {}
};

class BST {
public:
    Node* root;

    BST() : root(nullptr) {}

    void insert(int data) {
        Node* newNode = new Node(data);
        if (root == nullptr) {
            root = newNode;
            return;
        }

        Node* current = root;
        Node* parent = nullptr;

        while (current != nullptr) {
            parent = current;
            if (data < current->data) {
                current = current->left;
            } else {
                current = current->right;
            }
        }

        if (data < parent->data) {
            parent->left = newNode;
        } else {
            parent->right = newNode;
        }
    }

    void inorder() {
        if (root == nullptr) return;

        stack<Node*> s;
        Node* current = root;

        while (current != nullptr || !s.empty()) {
            while (current != nullptr) {
                s.push(current);
                current = current->left;
            }

            current = s.top();
            s.pop();

            cout << current->data << " ";

            current = current->right;
        }
    }

    Node* search(int key) {
        Node* current = root;

        while (current != nullptr && current->data != key) {
            if (key < current->data) {
                current = current->left;
            } else {
                current = current->right;
            }
        }

        return current;  // Will be nullptr if key not found
    }
};

int main() {
    BST tree;

    tree.insert(50);
    tree.insert(30);
    tree.insert(70);
    tree.insert(20);
    tree.insert(40);
    tree.insert(60);
    tree.insert(80);

    cout << "Inorder traversal: ";
    tree.inorder();
    cout << endl;

    int key = 40;
    Node* found = tree.search(key);
    if (found != nullptr) {
        cout << "Node with value " << key << " found in the tree." << endl;
    } else {
        cout << "Node with value " << key << " not found in the tree." << endl;
    }

    return 0;
}

