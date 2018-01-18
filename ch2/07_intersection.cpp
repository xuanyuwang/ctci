#include <iostream>
#include "./Node.cpp"

using namespace std;

bool isintersect(Node *A, Node *B){
  int lenA {0}, lenB{0};
  Node *it = nullptr;

  // length of A
  it = A;
  while(it){
    lenA += 1;
    it = it->next;
  }
  // length of B
  it = B;
  while(it){
    lenB += 1;
    it = it->next;
  }
  it = nullptr;

  cout << "Length of A: " << lenA << endl;
  cout << "Length of B: " << lenB << endl;

  //
  Node *longl = (lenA >= lenB)? A:B;
  Node *shortl = (lenA >= lenB)? B:A;
  int diff = (lenA >= lenB)? (lenA - lenB):(lenB - lenA);
  for(int i = 0; i < diff; i++){
    longl = longl->next;
  }

  while(longl && shortl){
    if(longl == shortl){
      return true;
    }
    longl = longl->next;
    shortl = shortl->next;
  }
  return false;
}

int main(){
  int data_A[] = {1,2,3,4,5};
  int data_B[] = {11};
  Node *A = new Node(data_A, 5);
  Node *B = new Node(data_B, 1);
  B->next = A->next->next;
  A->printList();
  B->printList();
  cout << boolalpha << isintersect(A, B) << endl;
  
}
