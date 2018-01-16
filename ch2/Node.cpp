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

