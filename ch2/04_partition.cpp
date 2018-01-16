#include <iostream>
#include "./Node.cpp"

void Partition(Node **list, int x){
  Node *it = *list;

  // initialize the new list
  Node *head = new Node(it->data);
  Node *tail = head;
  it = it->next;

  while(it != nullptr){
    Node *newNode = new Node(it->data);
    if(newNode->data >= x){
      tail->next = newNode;
      tail = newNode;
    }else{
      newNode->next = head;
      head = newNode;
    }
    it = it->next;
  }

  *list = head;
}

int main(){
  Node *head = new Node(1);
  int data[] = {3,5,8,5, 10, 2};
  for(auto i: data){
    Node *newNode = new Node(i);
    head->insert(newNode);
    std::cout << newNode->data << std::endl;
  }
  head->printList();
  
  Partition(&head, 5);
  head->printList();
}
