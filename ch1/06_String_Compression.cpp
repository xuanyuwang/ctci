#include <iostream>
#include <string>

using namespace std;

string compression(string testcase){
  string result = "";
  string::iterator it = testcase.begin();
  char current = *testcase.begin();
  int count = 1;
  result.append(&current, 1);
  cout << current;

  it++;
  while(it != testcase.end()){
    cout << *it;
    if(*it == *(it-1)){
      count++;
      it++;
    }else{
      result.append(to_string(count));
      result.append(&(*it), 1);
      count = 1;
      it++;
    }
  }
  result.append(to_string(count));
  cout << endl;

  return (result.length() >= testcase.length()) ? testcase: result;
}

int main(){
  string testcase = "aabcccccaaa";
  cout << "Tese case: " << testcase << endl;
  string result = compression(testcase);
  cout << "Result: " << result << endl;
}
