#include <iostream>
#include "./Node.cpp"
#include <stack>

using namespace std;

void isPalindrome(Node *head){
  if(head == nullptr || head->next == nullptr){
    cout << "True" << endl;
  }

  stack<Node*> nodeStack;
  Node *slow = head;
  Node *fast = head;
  nodeStack.push(slow);

  cout << "Initialization" << endl;
  cout << slow->data << fast->data << endl;

  cout << "Iteration" << endl;
  while(fast->next != nullptr && fast->next->next != nullptr){
    slow = slow->next;
    fast = fast->next->next;
    cout << slow->data << fast->data << endl;
    nodeStack.push(slow);
  }
  //for even length
  if(fast->next != nullptr && fast->next->next == nullptr){
    slow = slow->next;
    fast = fast->next;
    cout << "Even length" << endl;
  }else if(fast->next == nullptr){
    cout << "Odd length" << endl;
    slow = slow->next;
    nodeStack.pop();
  }
  cout << slow->data << fast->data << endl;

  //compare
  while(!nodeStack.empty()){
    Node* top = nodeStack.top();
    cout << "Compare " << top->data << " and " << slow->data << endl;
    if(top->data != slow->data){
      cout << "False" << endl;
      return;
    }
    slow = slow->next;
    nodeStack.pop();
  }
  cout << "True" << endl;
}


int main(){
  int data_p[] = {0,1,2, 2,1,0};
  //int data_p[] = {1,2,3,4,5,6,7};
  Node *testcase_p = new Node(data_p, 6);
  testcase_p->printList();

  isPalindrome(testcase_p);
}
