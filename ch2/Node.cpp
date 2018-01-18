#include <iostream>
using namespace std;

class Node{
public:
  int data = 0;
  Node *next = nullptr;

  Node(int val): data(val), next(nullptr) {}
  Node(int vals[], int size){
    data = vals[0];
    for(int i = 1; i < size; i++){
      Node *temp = new Node(vals[i]);
      this->insert(temp);
    }
  }
  ~Node(){}

  void insert(Node *n){
    Node *tail = this;
    while(tail->next != nullptr){
      tail = tail->next;
    }
    tail->next = n;
  }

  void printList(){
    Node *head = this;
    while(head){
      std::cout << head->data << "-->";
      head = head->next;
    }
    std::cout << "nullptr" << std::endl;
  }
};

