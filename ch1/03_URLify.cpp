#include <iostream>
#include <string>

using namespace std;

void urlify(char* str, int len){
  int numOfSpaces = 0;
  int i {0};
  for (i = 0; i < len; i++){
    if(str[i] == ' '){
      numOfSpaces++;
    }
  }

  int newLen = len + 2 * numOfSpaces;
  i = newLen - 1;
  for (int j = len - 1; j > 0; j--){
    if(str[j] != ' '){
      str[i] = str[j];
      i--;
    }else{
      str[i] = '0';
      str[i-1] = '2';
      str[i-2] = '%';
      i -= 3;
    }
  }
}

int main(){
  char str[] = "Mr John Smith    ";
  cout << "Actual String: " << str << endl;
  urlify(str, 13);
  cout << "URLified String: " << str << endl;
  return 0;
}

