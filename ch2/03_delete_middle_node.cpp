#include <iostream>
#include "Node.cpp"

void deleteNode(Node *n){
  Node *curr = n;
  Node *next = curr->next;
  while(next->next != nullptr){
    curr->data = next->data;
    std::cout << "Add " << curr->data << std::endl;
    curr = curr->next;
    next = next->next;
  }
  curr->data = next->data;
  std::cout << "Add " << curr->data << std::endl;
  curr->next = nullptr;
  delete next;
}

int main(){
  Node *head = new Node(1);
  int data[] = {2,3,4,5};
  for(auto i: data){
    Node *temp = new Node(i);
    head->insert(temp);
  }
  std::cout << "Before deletion" << std::endl;
  head->printList();
  deleteNode(head->next->next);
  std::cout << "After deletion" << std::endl;
  head->printList();
}
