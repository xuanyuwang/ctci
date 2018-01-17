#include <iostream>
#include "./Node.cpp"
#define BASE 10

using namespace std;

Node* add(Node *num1, Node *num2){
  int carry = 0;
  Node *result = nullptr;

  // Initialize the first digit of result
  result = new Node(num1->data + num2->data);
  cout << "Add " << num1->data << " and " << num2->data << " with carry " << carry << " = " << result->data << endl;
  carry = result->data >= BASE? 1:0;
  result->data = result->data % BASE;
  num1 = num1->next;
  num2 = num2->next;

  //Iteration
  Node *it = result;
  while(num1 || num2){
    int firstDigit = num1? num1->data:0;
    int secondDigit = num2? num2->data:0;
    Node *addition = new Node(firstDigit + secondDigit + carry);
    cout << "Add " << firstDigit << " and " << secondDigit << " with carry " << carry << " = " << addition->data << endl;
    carry = addition->data >= BASE? 1:0;
    addition->data = addition->data % BASE;
    it->next = addition;
    it = it->next;
    if(num1)num1 = num1->next;
    if(num2)num2 = num2->next;
  }

  return result;
}

int main(){
  Node *num1 = new Node(7);
  num1->next = new Node(1);
  num1->next->next = new Node(6);

  Node *num2 = new Node(5);
  num2->next = new Node(9);
  num2->next->next = new Node(2);

  cout << "First number: ";
  num1->printList();
  cout << "Second numebr: ";
  num2->printList();

  Node *result = add(num1, num2);
  result->printList();
}
