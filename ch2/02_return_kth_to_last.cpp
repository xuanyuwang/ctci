#include <iostream>

using namespace std;

class Node{
public:
  int val;
  Node* next;
  Node(int n): val(n), next(nullptr){};
  void show(){
    cout << " " << val << " ";
  }
};

int main(){
  Node* a = new Node(1);
  Node* b = new Node(2);
  Node* c = new Node(3);
  Node* d = new Node(4);
  Node* e = new Node(5);
  Node* f = new Node(6);
  a->next = b;
  b->next = c;
  c->next = d;
  d->next = e;
  e->next = f;

  int k = 2;
  Node *p1, *p2;
  p1 = a;
  p2 = a;
  for(int i = 1; i < k; i++){
    p2 = p2->next;
  }

  while(p2->next != nullptr){
    p1 = p1->next;
    p2 = p2->next;
  }

  p1->show();
}

  
