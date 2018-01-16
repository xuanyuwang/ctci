#include <iostream>
#include <unordered_map>
#include <random>
#include <vector>

class Node{
public:
  int data = 0;
  Node *next = nullptr;

  Node(int val): data(val), next(nullptr) {}
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

void removeDuplicates(Node *head){
  // If the linked list is empty, or only has one node
  if(head == nullptr || (head && (head->next == nullptr))){
    return;
  }

  std::unordered_map<int, int> node_map;
  Node *prev = head;
  Node *curr = head->next;
  node_map[head->data] = 1;
  while(curr != nullptr){
    // find a node whose value is unique
    while(curr && node_map.find(curr->data) != node_map.end()){
      curr = curr->next;
    }
    // jump to the node and ignore the middle ones
    prev->next = curr;
    prev = curr;
    if(curr){
      node_map[curr->data] = 1;
      curr = curr->next;
    }
  }
}

int main(){
  std::cout << "Method 1:\n" << std::endl;
  int data[] = {1,2,3,4,5,6,4,3,2};
  Node *head = new Node(0);
  for(auto i: data){
    Node *temp = new Node(i);
    head->insert(temp);
  }
  head->printList();
  removeDuplicates(head);
  head->printList();
}
